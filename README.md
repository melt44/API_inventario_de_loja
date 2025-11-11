# 📦 API de Controle de Inventário

![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.0-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-336791?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-24.0.5-2496ED?style=flat&logo=docker&logoColor=white)

Uma API RESTful assíncrona e de alta performance para gerenciamento de inventário, desenvolvida com **FastAPI**, **SQLModel** e **PostgreSQL**, totalmente containerizada com **Docker**.

Este projeto demonstra a aplicação de conceitos modernos de Engenharia de Software, como validação de dados, ORM assíncrono, arquitetura em camadas e orquestração de contêineres.

## ✨ Funcionalidades

O sistema oferece um CRUD (Create, Read, Update, Delete) completo:

- **Cadastro de Produtos**: Adição de itens com validação automática de campos (preço positivo, nome obrigatório, etc.).
- **Consulta**: Listagem geral de inventário e busca detalhada por ID.
- **Atualização**: Alteração de dados de produtos existentes.
- **Remoção**: Exclusão de itens do banco de dados.
- **Persistência**: Dados salvos em banco relacional (PostgreSQL) via volumes Docker.

## 🛠️ Tecnologias Utilizadas

- **[Python 3.11+](https://www.python.org/)**: Linguagem base.
- **[FastAPI](https://fastapi.tiangolo.com/)**: Framework web moderno e rápido para construção de APIs.
- **[SQLModel](https://sqlmodel.tiangolo.com/)**: Biblioteca que une SQLAlchemy e Pydantic para interagir com bancos SQL de forma intuitiva.
- **[PostgreSQL](https://www.postgresql.org/)**: Banco de dados relacional robusto.
- **[Asyncpg](https://github.com/MagicStack/asyncpg)**: Driver de banco de dados assíncrono para alta performance.
- **[Docker & Docker Compose](https://www.docker.com/)**: Para criação de ambientes isolados e reprodutíveis.

## 🚀 Como Executar o Projeto

### Pré-requisitos

Você precisa ter instalado apenas:
- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/)

### Passo a Passo

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
   cd nome-do-repositorio

1. **Configure as Variáveis de Ambiente:**
    Crie um arquivo chamado .env na raiz do projeto e adicione as configurações do banco (você pode alterar a senha se desejar):

    DB_USER=admin
    DB_PASSWORD=sua_senha_aqui
    DB_NAME=inventario_db
    DATABASE_URL=postgresql+asyncpg://admin:sua_senha_aqui@db:5432/inventario_db

3. **Inicie a Aplicação:**
    Execute o comando abaixo para construir as imagens e subir os contêineres:

    docker-compose up --build

4. **Acesse a API:**
    Aguarde os logs indicarem que o servidor está rodando. A API estará disponível em: http://localhost:8000

## 📖 Documentação (Swagger UI)
O FastAPI fornece documentação interativa automática. Com o projeto rodando, acesse:

## 👉 http://localhost:8000/docs

Lá você pode testar todas as rotas (GET, POST, PUT, DELETE) diretamente pelo navegador, ver os esquemas de dados e as respostas esperadas.

## 🧪 Exemplo de Uso (Curl)
Você também pode testar via terminal. Exemplo para adicionar um item:

Bash

curl -X 'POST' \
  '[http://127.0.0.1:8000/itens/](http://127.0.0.1:8000/itens/)' \
  -H 'Content-Type: application/json' \
  -d '{
  "nome": "Notebook Gamer",
  "descricao": "i7, 16GB RAM, RTX 3060",
  "preco": 4500.00,
  "quantidade": 5
}'
## 📂 Estrutura do Projeto
.
├── app/
│   ├── __init__.py
│   ├── main.py          # Ponto de entrada e rotas da API
│   ├── models.py        # Modelos de dados (SQLModel)
│   └── database.py      # Configuração de conexão com o DB
├── docker-compose.yml   # Orquestração dos serviços (API + DB)
├── Dockerfile           # Definição da imagem da aplicação
├── requirements.txt     # Dependências do Python
└── README.md            # Documentação