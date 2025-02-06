# Usa la imagen base de Python 3.13.1 con Bookworm
FROM python:3.13.1-bookworm

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia solo los archivos necesarios para instalar dependencias primero (optimización de cache)
COPY requirements.txt ./

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente después de instalar dependencias
COPY . /app

# Expone el puerto 8000 para FastAPI
EXPOSE 8182

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8182", "--reload"]
