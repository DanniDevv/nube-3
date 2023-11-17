# Usa una imagen Python más liviana
FROM python:3-slim

# Instala la dependencia necesaria
RUN pip install pandas flask redis

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY app.py /app/
COPY movies.csv /app/
COPY ratings.csv /app/

# Establece el punto de entrada
CMD ["python", "app.py"]
