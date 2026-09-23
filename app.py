import os
import requests

from dotenv import load_dotenv

load_dotenv()

api=os.getenv("api_key")

titulo = input("Digite o nome do filme que você quer saber mais: ")

url = "http://www.omdbapi.com/"
params = {
    "apikey": api,
    "t": titulo
}

resposta = requests.get(url, params=params)

dados = resposta.json()

print(dados)