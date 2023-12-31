# Imagen Base
FROM python:3.10.4-slim-bullseye

# Setear Variables de Entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Setear directorio de trabajo
WORKDIR /code

# Instalar Dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copiar el proyecto
COPY . .