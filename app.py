import os
import requests
from flask import Flask, render_template, request

from dotenv import load_dotenv

load_dotenv()

api=os.getenv("api_key")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    dados = None
    erro = None

    if request.method == "POST":
        titulo = request.form.get("título")

        url = "http://www.omdbapi.com/"
        params = {
            "apikey": api,
            "t": titulo
        }

        resposta = requests.get(url, params=params)
        resultado = resposta.json()

        if resultado.get("Response") == "True":
            dados = resultado

        else:
            erro = resultado.get("Erro", "Filme não encontrado")

    return render_template("index.html", dados=dados, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)