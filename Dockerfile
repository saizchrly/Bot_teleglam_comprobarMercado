# Usa una imagen base que tenga Python instalado
FROM python:3.8.10

# Establece el directorio de trabajo en el contenedor
WORKDIR /

# Copia los archivos Python al directorio de trabajo del contenedor
COPY . /

# Instala las dependencias si es necesario (por ejemplo, requirements.txt)
RUN pip install -r requirements.txt

# Ejecuta tu programa cuando se inicie el contenedor
CMD ["python3", "LectorMercado.py"]
