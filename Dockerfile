# Imagen base de Python (misma version que el venv local)
FROM python:3.14-slim

# curl se usa para el healthcheck en produccion
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Evitar archivos .pyc y ver los logs al instante
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar requirements y instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el codigo de la aplicacion
COPY . .

# Exponer el puerto 
EXPOSE 8000

# Comando por defecto (dev y prod lo sobrescriben en su compose)
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
