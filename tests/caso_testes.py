casos_de_teste = [
    {"id": "PRIV-01", "pergunta": "Qual é a legislação principal que fundamenta a política de privacidade do Voa Bank?",
     "resposta_esperada": "A Lei Geral de Proteção de Dados (Lei nº 13.709/2018 - LGPD)."},

    {"id": "PRIV-02", "pergunta": "Por quanto tempo o Voa Bank mantém o histórico de transações dos clientes?",
     "resposta_esperada": "10 anos, conforme exigência do Banco Central (BACEN)."},

    {"id": "PRIV-03", "pergunta": "Se eu quiser solicitar a exclusão dos meus dados pessoais, qual o prazo de resposta e por qual canal devo pedir?",
     "resposta_esperada": "Pelo aplicativo, em 'Configurações > Privacidade e Dados', ou pelo e-mail dpo@voabank.com.br. Prazo de até 15 dias úteis."},

    {"id": "PRIV-04", "pergunta": "Com quais birôs de crédito o Voa Bank pode compartilhar meus dados para análise de crédito?",
     "resposta_esperada": "Serasa Experian e Boa Vista SCPC."},

    {"id": "PRIV-05", "pergunta": "Qual tipo de criptografia o Voa Bank usa para dados em trânsito?",
     "resposta_esperada": "TLS 1.3."},

    {"id": "PRIV-06", "pergunta": "O Voa Bank vende dados de clientes para empresas de marketing?",
     "resposta_esperada": "Não. O documento afirma explicitamente que o Voa Bank não vende dados pessoais a terceiros para fins de marketing."},

    {"id": "TERMOS-01", "pergunta": "Qual a idade mínima para abrir uma conta no Voa Bank sem autorização de responsável legal?",
     "resposta_esperada": "18 anos. Entre 16 e 18 anos é permitido com autorização de responsável legal (conta Voa Jovem)."},

    {"id": "TERMOS-02", "pergunta": "O Voa Bank pode reduzir o limite do meu cartão de crédito sem aviso prévio?",
     "resposta_esperada": "Em geral não, exige aviso prévio de 15 dias. Exceção: suspeita de fraude ou inadimplência, onde a redução pode ser imediata."},

    {"id": "TERMOS-03", "pergunta": "O saldo em conta no Voa Bank é considerado depósito bancário?",
     "resposta_esperada": "Não. É segregado patrimonialmente conforme regulação do BACEN para instituições de pagamento."},

    {"id": "TERMOS-04", "pergunta": "Em quais situações o Voa Bank pode encerrar minha conta sem dar aviso prévio de 30 dias?",
     "resposta_esperada": "Suspeita fundamentada de fraude/lavagem de dinheiro/financiamento ao terrorismo; determinação legal ou regulatória; uso indevido comprovado."},

    {"id": "TERMOS-05", "pergunta": "Qual o número da central telefônica de atendimento do Voa Bank?",
     "resposta_esperada": "0800 555 0199 (ligação gratuita)."},

    {"id": "FAQ-01", "pergunta": "Qual o limite diário de Pix durante a noite (período noturno)?",
     "resposta_esperada": "R$ 1.000,00, válido das 20h às 6h, para novos usuários."},

    {"id": "FAQ-02", "pergunta": "Se eu aumentar meu limite de Pix para R$ 15.000,00, o aumento vale imediatamente?",
     "resposta_esperada": "Não. Aumentos acima de R$ 10.000,00 têm carência de 24 horas (Resolução BCB nº 150/2021)."},

    {"id": "FAQ-03", "pergunta": "É possível cancelar um Pix depois de enviado?",
     "resposta_esperada": "Não. Pode-se acionar o Mecanismo Especial de Devolução (MED) em até 80 dias em caso de fraude ou erro."},

    {"id": "FAQ-04", "pergunta": "Fiz uma compra internacional de US$ 100 no cartão de crédito. Quanto de IOF incide sobre essa transação?",
     "resposta_esperada": "IOF de 3,38% sobre o valor da transação internacional no cartão de crédito (não confundir com o IOF de 0,38% de remessa internacional/câmbio)."},

    {"id": "FAQ-05", "pergunta": "Até que horas um boleto precisa ser pago para ser processado no mesmo dia?",
     "resposta_esperada": "Até às 20h30 (horário de Brasília)."},

    {"id": "FAQ-06", "pergunta": "Existe algum limite para receber dinheiro via Pix?",
     "resposta_esperada": "Não há limite para recebimento de Pix. Limites se aplicam apenas a valores enviados."},

    {"id": "SEG-01", "pergunta": "O Voa Bank atende clientes por WhatsApp?",
     "resposta_esperada": "Não. Canal oficial é o chat do aplicativo ou 0800 555 0199."},

    {"id": "SEG-02", "pergunta": "Em quantos dias posso acionar o Mecanismo Especial de Devolução (MED) após uma fraude via Pix?",
     "resposta_esperada": "Até 80 dias após a transação."},

    {"id": "SEG-03", "pergunta": "O Voa Bank ressarce valores em qualquer caso de fraude?",
     "resposta_esperada": "Não em todos os casos. Ressarcimento integral só para falha de segurança da plataforma, não para engenharia social onde o usuário forneceu credenciais voluntariamente. Prazo de até 10 dias úteis."},

    {"id": "SEG-04", "pergunta": "O que é o golpe de 'SIM Swap' mencionado na política de segurança?",
     "resposta_esperada": "Transferência da linha telefônica da vítima para chip do criminoso, interceptando SMS de autenticação. Recomenda-se TOTP ou biometria em vez de SMS."},

    {"id": "SEG-05", "pergunta": "Quais tipos de autenticação de dois fatores são obrigatórios no Voa Bank?",
     "resposta_esperada": "2FA obrigatório para: alteração de senha, cadastro de nova chave Pix, aumento de limites e alteração de dados cadastrais."},

    {"id": "TAR-01", "pergunta": "Qual a mensalidade da conta Voa Bank Plus?",
     "resposta_esperada": "R$ 14,90 por mês (isenta com movimentação mínima de R$ 1.000/mês)."},

    {"id": "TAR-02", "pergunta": "Quanto custa uma TED na conta Voa Bank Light?",
     "resposta_esperada": "R$ 8,90 por transferência."},

    {"id": "TAR-03", "pergunta": "Comparando os três planos, qual oferece TED gratuita ilimitada?",
     "resposta_esperada": "Voa Bank Black. Plus oferece só até 5/mês grátis (depois R$ 6,90); Light cobra R$ 8,90 sempre."},

    {"id": "TAR-04", "pergunta": "Qual a taxa de juros rotativo do cartão de crédito no plano Voa Bank Black?",
     "resposta_esperada": "Até 11,90% ao mês."},

    {"id": "TAR-05", "pergunta": "Quanto custa sacar dinheiro em rede conveniada (Banco24Horas) com o cartão de débito?",
     "resposta_esperada": "R$ 6,50 por saque, sendo o primeiro saque do mês gratuito."},

    {"id": "TAR-06", "pergunta": "Qual a tarifa de manutenção da conta Voa Bank Light se eu não movimentar nenhum valor no mês?",
     "resposta_esperada": "Gratuita, sem exigência de movimentação mínima (diferente de Plus e Black)."},

    {"id": "MULTI-01", "pergunta": "Se eu suspeitar que minha conta foi usada por terceiros para receber e repassar dinheiro rapidamente (conta laranja), o que pode acontecer com minha conta?",
     "resposta_esperada": "Bloqueio preventivo (Política de Segurança) e possível encerramento sem aviso prévio de 30 dias, com comunicação às autoridades (Termos de Uso)."},

    {"id": "MULTI-02", "pergunta": "O Voa Bank pode bloquear minha conta por determinação de autoridades? Quais autoridades são mencionadas nos documentos?",
     "resposta_esperada": "Sim. BACEN, COAF, Receita Federal (Privacidade) e Poder Judiciário (Segurança)."},

    {"id": "TRAP-GERAL-01", "pergunta": "Qual o valor do CDI usado pelo Voa Bank para render o saldo em conta?",
     "resposta_esperada": "Não disponível nos documentos. Os Termos mencionam rendimento ao CDI, mas sem especificar percentual. Resposta correta é admitir que não sabe."},

    {"id": "TRAP-GERAL-02", "pergunta": "O Voa Bank tem agências físicas para atendimento presencial?",
     "resposta_esperada": "Não mencionado nos documentos. Só há referência a 'agência parceira' para emissão de extrato impresso — não confirma nem nega rede própria de agências."},
]

print(f"Total de casos de teste: {len(casos_de_teste)}\n")
print("=" * 100)

resultados = []

for caso in casos_de_teste:
    resposta_obtida = rag_chain.invoke(caso["pergunta"])

    resultados.append({
        "id": caso["id"],
        "pergunta": caso["pergunta"],
        "resposta_esperada": caso["resposta_esperada"],
        "resposta_obtida": resposta_obtida,
    })

    print(f"[{caso['id']}]")
    print(f"Pergunta: {caso['pergunta']}")
    print(f"Esperado: {caso['resposta_esperada']}")
    print(f"Obtido:   {resposta_obtida}")
    print("-" * 100)

print("\nTeste concluído. Resultados salvos na variável 'resultados' para análise posterior.")