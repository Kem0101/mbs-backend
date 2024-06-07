# Usar imagen base de python
FROM python:3.10-slim

# Manejos de logs como en django local al hacer docker run
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar las dependencias necesarias
RUN apt-get update && \
  apt-get install -y netcat-openbsd build-essential gcc libmariadb-dev pkg-config && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

# Copiar los archivos de requerimientos al contenedor
COPY requirements.txt ./
COPY manage.py ./
COPY config ./config
COPY mbs ./mbs

# Instalar las dependencias de Python
RUN pip install -r requirements.txt

# Copiar todo el proyecto al directorio de trabajo
COPY ./ ./

# Exponer el puerto en el que Django correrá
EXPOSE 8001

# Comando por defecto para ejecutar el servidor de desarrollo
CMD ["watchmedo", "auto-restart", "--directory=.", "python3", "manage.py", "runserver", "0.0.0.0:8001"]
