# Usa una imagen base que tenga Python instalado
FROM python:3.8.10

# Establece el directorio de trabajo en el contenedor
WORKDIR /Bot

# Copia los archivos Python al directorio de trabajo del contenedor
COPY /src /Bot
COPY bibliotecas.txt /Bot
COPY LectorMercado.py /Bot

# Instala las dependencias si es necesario (por ejemplo, requirements.txt)
RUN pip install -r bibliotecas.txt

# Ejecuta tu programa cuando se inicie el contenedor
CMD ["python3", "LectorMercado.py"]
