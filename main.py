from scrapy import get_token, get_contas_a_pagar, get_historico


cpf_cnpj = '' # somente os numeros #
password = ''  # senha do site #

try:
    token = get_token(cpf_cnpj, password)
    get_contas_a_pagar(token) # gera o arquico => contas_a_pagar.csv
    get_historico(token)  # gera o arquico => historico.csv
except Exception as e:
    print("Erro: ", e)