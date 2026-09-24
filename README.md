# API de Filmes

Aplicação web desenvolvida em **Python** utilizando **Flask** para consultar informações de filmes através da **OMDb API**.

O usuário informa o título de um filme e a aplicação realiza uma requisição à API, processa os dados retornados e apresenta as principais informações do filme em uma interface web.

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge\&logo=flask\&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2E7D32?style=for-the-badge\&logo=python\&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)
![python-dotenv](https://img.shields.io/badge/python--dotenv-ECD53F?style=for-the-badge\&logo=python\&logoColor=black)
![OMDb API](https://img.shields.io/badge/OMDb%20API-000000?style=for-the-badge)
![Render](https://img.shields.io/badge/Render-46E3B7?style=for-the-badge\&logo=render\&logoColor=black)

## Aplicação online

A aplicação está disponível para acesso através do Render:

[![Acessar aplicação](https://img.shields.io/badge/Acessar%20Aplicação-API%20de%20Filmes-000000?style=for-the-badge)](https://api-filme-1hka.onrender.com/)

**Acesse:** https://api-filme-1hka.onrender.com/

## Sobre o projeto

O projeto foi desenvolvido para praticar o consumo de **APIs externas em Python** e a criação de uma aplicação web utilizando Flask.

A aplicação recebe o nome do filme através de um formulário HTML e realiza uma requisição `GET` para a OMDb API.

Após receber a resposta em JSON, os dados são processados e exibidos na página.

Entre as informações apresentadas estão:

* Título do filme.
* Ano de lançamento.
* Pôster.
* Diretor.
* Sinopse.
* Nota IMDb.
* Bilheteria.

Caso o filme não seja encontrado, uma mensagem de erro é apresentada ao usuário.

## Como funciona

```text
Usuário
   │
   ▼
Interface HTML
   │
   ▼
Flask
   │
   ▼
Requisição HTTP
   │
   ▼
OMDb API
   │
   ▼
Resposta JSON
   │
   ▼
Flask processa os dados
   │
   ▼
Informações do filme
```

A aplicação utiliza a biblioteca `requests` para realizar a requisição HTTP e `python-dotenv` para carregar a chave da API a partir do arquivo `.env`.

## Funcionalidades

* Busca de filmes pelo título.
* Consumo de API externa.
* Processamento de dados em JSON.
* Exibição de informações do filme.
* Exibição do pôster.
* Tratamento de filme não encontrado.
* Interface web com HTML e CSS.
* Utilização de variável de ambiente para proteger a chave da API.
* Aplicação publicada na internet através do Render.

## Estrutura do projeto

```text
API_filme/
│
├── static/
│   ├── favicon.png
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .gitignore
└── app.py
```

### Descrição dos arquivos

| Arquivo                | Função                                          |
| ---------------------- | ----------------------------------------------- |
| `app.py`               | Aplicação Flask e lógica de consulta à API      |
| `templates/index.html` | Interface e exibição dos resultados             |
| `static/style.css`     | Estilos da aplicação                            |
| `static/favicon.png`   | Ícone da aplicação                              |
| `.gitignore`           | Arquivos e pastas que não devem ser versionados |

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/leonardodiello/API_filme.git
```

Entre na pasta:

```bash
cd API_filme
```

### 2. Crie um ambiente virtual

No macOS/Linux:

```bash
python3 -m venv venv
```

Ative o ambiente:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install Flask requests python-dotenv
```

### 4. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

```env
api_key=SUA_CHAVE_DA_OMDB_API
```

A chave é carregada pelo `app.py` através do `python-dotenv`.

**Não compartilhe sua chave da API e não envie o arquivo `.env` para o GitHub.**

O `.gitignore` do projeto deve manter o `.env` fora do versionamento.

## Executando o projeto localmente

Com o ambiente virtual ativado e o `.env` configurado, execute:

```bash
python app.py
```

A aplicação Flask será iniciada localmente.

Depois, acesse no navegador:

```text
http://127.0.0.1:5000
```

## Utilização

Na página inicial:

1. Digite o nome do filme em inglês.
2. Clique em **Buscar**.
3. A aplicação consulta a OMDb API.
4. Os dados encontrados são exibidos na página.

Por exemplo:

```text
The Batman
```

O resultado apresenta as informações retornadas pela API, incluindo título, ano, pôster, diretor, sinopse, nota IMDb e bilheteria.

## Deploy

O projeto foi publicado utilizando o **Render**, permitindo que a aplicação Flask seja acessada diretamente pela internet.

### Aplicação

```text
https://api-filme-1hka.onrender.com/
```

O deploy permite testar o projeto sem precisar configurar o ambiente Python localmente.

## Exemplo de requisição

A aplicação utiliza o endpoint da OMDb API:

```text
http://www.omdbapi.com/
```

Os parâmetros enviados são:

```python
params = {
    "apikey": api,
    "t": titulo
}
```

A resposta da API é convertida para JSON:

```python
resultado = resposta.json()
```

Quando a API retorna uma resposta válida, os dados são enviados para o template:

```python
dados = resultado
```

Caso contrário, a aplicação apresenta uma mensagem informando que o filme não foi encontrado.

## Conceitos praticados

Este projeto foi desenvolvido para praticar:

* Python.
* Flask.
* Rotas.
* Requisições HTTP.
* Consumo de APIs REST.
* Manipulação de JSON.
* Variáveis de ambiente.
* `python-dotenv`.
* Biblioteca `requests`.
* Templates com Jinja2.
* HTML e CSS.
* Tratamento básico de erros.
* Integração entre back-end e front-end.
* Deploy de aplicação web.

## Objetivo

O objetivo do projeto é praticar o desenvolvimento de aplicações web com **Python e Flask**, principalmente o consumo de APIs externas, processamento de dados JSON, integração entre back-end e interface web e publicação de uma aplicação em um ambiente de hospedagem.

## Autor

**Leonardo Diello Charão**

Estudante de Engenharia de Software — IFAM.

[![GitHub](https://img.shields.io/badge/GitHub-leonardodiello-181717?style=for-the-badge\&logo=github)](https://github.com/leonardodiello)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Leonardo%20Diello-0A66C2?style=for-the-badge\&logo=linkedin)](https://www.linkedin.com/in/leonardo-diello/)
