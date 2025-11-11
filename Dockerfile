# 1. Começamos com uma imagem Python oficial
FROM python:3.11-slim

# 2. Definimos o diretório de trabalho dentro do contêiner
WORKDIR /app

# 3. Copiamos o arquivo de dependências
COPY requirements.txt .

# 4. Instalamos as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos o código da nossa aplicação (a pasta 'app')
COPY ./app /app

# 6. Comando para executar a API quando o contêiner iniciar
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]