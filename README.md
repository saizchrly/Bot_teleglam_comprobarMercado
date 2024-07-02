[![codebeat badge](https://codebeat.co/badges/671e4983-43e3-42a2-814f-1add9beab322)](https://codebeat.co/projects/github-com-saizchrly-bot_teleglam_comprobarmercado-main)[![codecov](https://codecov.io/github/saizchrly/Bot_teleglam_comprobarMercado/graph/badge.svg?token=1HPB6YPI7A)](https://codecov.io/github/saizchrly/Bot_teleglam_comprobarMercado)

# Bot Lector de Mercado
Este es un bot de Telegram, desarrollado por el momento para ejecutarse en máquinas Linux, enfocado en la lectura de los datos de las acciones que el usuario ha introducido con anterioridad.
Está desarrollado principalmente con la librería *python-telegram-bot*, aunque se apoya en otras librerías para la ejecución de los comandos, como la librería *yfinance*, para la obtención de los datos de las acciones en el mercado

## Método de ejecución
1. CLONAR REPOSITORIO
```
git clone URL nombre_directorio_destino
```
2. INSTALACIÓN DOCKER<br>
Primero de todo debes tener en el equipo docker, si ya posees docker en tu equipo puedes saltar el paso 3.
Si no lo tienes puedes descargarlo de dos formas, la version gráfica, [link](https://www.docker.com/products/docker-desktop/), o si deseas descargarlo por línea de comandos en linux, [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04-es)

3. CONFIGURAR BOT<br>
No debemos olvidar que antes de realizar la imagen debemos al menos actualizar el archivo **Bot_telegram.txt** con la dirección de nuestro bot

4. CREAR LA IMAGEN
```
docker build -t nombre:1 .
```
5. RUN DE LA IMAGEN
```
docker run nombre:1
```

## Ayuda 
Si tiene alguna duda de la función de los comandos o no sabe que comando debe ejecutar para obtener los resultados escriba dentro del chat con el bot.
```
/help
```
Esto desplegará una lista de los comandos que se encuentran activos.

## Colaboradores
<p style="text-align: center;">SaizCharly</p