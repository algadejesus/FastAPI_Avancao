FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Arquivos de ambientes
ENV PYTHONUNBUFFERED=1
ENV PATH="/root/.local/bin:$PATH"
ENV PYTHONPATH='/'

# Copiar arquivos do Poetry
COPY ./poetry.lock ./pyproject.toml ./

# Instalação de pacotes
RUN apt-get update -y \
    && apt-get install -y curl build-essential python3-dev \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install -vvv \
    && apt-get remove -y curl \
    && apt-get autoremove -y

# Copiar o código fonte da aplicação
COPY ./app /app

# Definir o diretório de trabalho novamente
WORKDIR /app
