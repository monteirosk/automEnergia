import requests
import pandas as pd



BASE_URL = 'https://api.amazonasenergia.com/api/'


def get_token(cnpj, senha):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://agencia.amazonasenergia.com',
        'Pragma': 'no-cache',
        'Referer': 'https://agencia.amazonasenergia.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    
    }

    json_data = {
        'cpf_cnpj': cnpj,
        'password': senha,
    }

    response = requests.post(BASE_URL + 'authentication/login', headers=headers, json=json_data)
    return response.json()['token']



def get_contas_a_pagar(Token):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Bearer ' + Token,
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://agencia.amazonasenergia.com',
        'Pragma': 'no-cache',
        'Referer': 'https://agencia.amazonasenergia.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get( BASE_URL + 'faturas?situacao[]=ABER&situacao[]=REAV&situacao[]=TRAN', headers=headers,)
    df = pd.json_normalize(response.json())
    df.to_csv('contas_a_pagar.csv', index=False, sep=';', decimal=',')
    return df


def get_historico(Token):
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Bearer ' + Token,
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Origin': 'https://agencia.amazonasenergia.com',
        'Pragma': 'no-cache',
        'Referer': 'https://agencia.amazonasenergia.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get( BASE_URL + 'faturas?situacao[]=PAGA&situacao[]=PAGR', headers=headers)

    df = pd.json_normalize(response.json())
    df.to_csv('historico.csv', index=False, sep=';', decimal=',')
    return df




