import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import re
from docling.document_converter import DocumentConverter
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_huggingface import HuggingFaceEmbeddings

api_key = st.secrets["OPENROUTER_API_KEY"]


converter = DocumentConverter()


def limpar(s):
    s = s.replace("**", "").replace("<br>", " ")
    return s.strip()


def extrair_texto_e_tabelas(caminho_pdf):
 
    result = converter.convert(caminho_pdf)
    texto_md = result.document.export_to_markdown()
    linhas = texto_md.split("\n")

    texto_sem_tabelas = []
    documentos_tabelas = []
    buffer_tabela = []

    def processar_buffer_tabela():
        linhas_tabela = [l for l in buffer_tabela if not re.match(r"^\|[\s\-:|]+\|$", l.strip())]
        celulas = [[limpar(c) for c in l.strip().strip("|").split("|")] for l in linhas_tabela]
        if len(celulas) < 2:
            return
        cabecalho = celulas[0]
        for linha in celulas[1:]:
            partes = [
                f"{cabecalho[j]}: {linha[j]}"
                for j in range(min(len(cabecalho), len(linha)))
                if linha[j]
            ]
            if partes:
                frase = " | ".join(partes) + "."
                documentos_tabelas.append(Document(
                    page_content=frase,
                    metadata={"source": caminho_pdf, "tipo": "tabela"}
                ))

    for linha in linhas:
        if linha.strip().startswith("|"):
            buffer_tabela.append(linha)
        else:
            if buffer_tabela:
                processar_buffer_tabela()
                buffer_tabela = []
            texto_sem_tabelas.append(limpar(linha))

    if buffer_tabela:
        processar_buffer_tabela()

    documento_texto = Document(
        page_content="\n".join(texto_sem_tabelas),
        metadata={"source": caminho_pdf, "tipo": "texto"}
    )

    return documento_texto, documentos_tabelas

caminhos_pdfs = [
    r"data/documentos_fonte/01_politica_privacidade_protecao_dados.pdf",
    r"data/documentos_fonte/02_termos_condicoes_uso.pdf",
    r"data/documentos_fonte/03_faq_transacoes_limites.pdf",
    r"data/documentos_fonte/04_politica_seguranca_prevencao_fraudes.pdf",
    r"data/documentos_fonte/05_tarifas_comissoes.pdf",
]

documentos_texto = []
documentos_tabelas = []

for caminho in caminhos_pdfs:
    doc_texto, docs_tab = extrair_texto_e_tabelas(caminho)
    documentos_texto.append(doc_texto)
    documentos_tabelas.extend(docs_tab)

print(f"Documentos de texto: {len(documentos_texto)}")
print(f"Chunks de tabela (já prontos, um por linha): {len(documentos_tabelas)}")


text_splitter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=100)
splits_texto = text_splitter.split_documents(documentos_texto)

all_splits = splits_texto + documentos_tabelas

print(f"Chunks de texto: {len(splits_texto)}")
print(f"Chunks de tabela: {len(documentos_tabelas)}")
print(f"Total combinado: {len(all_splits)}")

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_store = InMemoryVectorStore(embeddings)
vector_store.add_documents(documents=all_splits)
print(f"Indexed {len(all_splits)} chunks.")


retriever = vector_store.as_retriever(search_kwargs={"k": 6})

# llm = ChatOllama(model="llama3.1", temperature=0)

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0, google_api_key=st.secrets["OPENROUTER_API_KEY"])

prompt = ChatPromptTemplate.from_template("""
Você é um assistente do Voa Bank. Responda a pergunta do colaborador
usando APENAS o contexto abaixo.

Leia todos os trechos do contexto com atenção antes de responder.
Se o contexto afirmar ou negar algo relacionado à pergunta, isso é uma resposta válida
e você deve respondê-la normalmente — inclusive se a resposta for "não" ou uma negação.
Só diga que não encontrou a informação se o assunto da pergunta realmente não for
mencionado em nenhum trecho do contexto.

Quando o contexto descrever uma REGRA GERAL e também uma EXCEÇÃO a essa regra,
responda com base na regra geral primeiro, e mencione a exceção em seguida.
Não responda "sim" apenas porque uma exceção existe, se a regra geral for "não".

Sempre justifique sua resposta com uma frase curta baseada no contexto, para que o
colaborador possa verificar a fonte da informação. Não responda apenas "sim" ou "não"
sem explicação.

Base de informações:
{base}

Pergunta: {pergunta}

Resposta:
""")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"base": retriever | format_docs, "pergunta": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

st.title("Voa Bank — Assistente de Compliance")

if "mensagens" not in st.session_state:
    st.session_state.mensagens = []

for msg in st.session_state.mensagens:
    st.chat_message(msg["role"]).write(msg["content"])

pergunta = st.chat_input("Pergunte sobre políticas do Voa Bank...")
if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})
    st.chat_message("user").write(pergunta)
    resposta = rag_chain.invoke(pergunta)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    st.chat_message("assistant").write(resposta)