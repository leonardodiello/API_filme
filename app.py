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

if dados.get("Response") == "True":
    print(f"Título: {dados['Title']}")
    print(f"Ano: {dados['Year']}")
    print(f"Diretor: {dados['Director']}")
    print(f"Sinopse: {dados['Plot']}")
    print(f"Nota IMDb: {dados['imdbRating']}")
    print(f"Pôster: {dados['Poster']}")
else:
    print(f"Erro: {dados.get('Error', 'Filme não encontrado')}")