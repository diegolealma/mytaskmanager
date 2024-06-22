# Dockerfile

# Usar uma imagem oficial do Python como a base
FROM python:3.9

# Configurar o diretório de trabalho dentro do container
WORKDIR /code

# Copiar os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o diretório de trabalho
COPY . .

# Expôr a porta que o servidor Django usará
EXPOSE 8000

# Comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
