# Bot Lector de Mercado
Este es un bot de Telegram, desarrollado por el momento para ejecutarse en máquinas Linux, enfocado en la lectura de los datos de las acciones que el usuario ha introducido con anterioridad.
Está desarrollado principalmente con la librería *python-telegram-bot*, aunque se apoya en otras librerías para la ejecución de los comandos, como la librería *yfinance*, para la obtención de los datos de las acciones en el mercado

## Método de ejecución
1. **Clonar el repositorio en la máquina** en la que deseemos que se ejecute el bot, recordar que para tener una disponibilidad completa la máquina ha de estar encendida y ejecutando el bot

2. **Crear un bot de Telegram**, si ya poseemos uno y es el que queremos usar pasar al paso 3.
Si por el contrario no tenemos ninguno, o queremos crear uno nuevo, sigue los pasos del [link](https://smartbotsland.com/create-edit-bot/get-token-botfather-telegram/), posteriormente obtendremos el token del bot

3. **Configurar el bot**, una vez ya tenemos el token del bot que queremos usar, lo copiaremos en la [ruta](Configuracion\Bot_telegram.txt) *Bot_teteglam_comprobarMercado\Configuracion\Bot_telegram.txt*

4. **Ejecutaremos el archivo de bash, [instalar.sh](instalar.sh)**, Recuerde que es un programa pensado para ejecutarse en una máquina Linux
```
$ ./instalar.sh
```

5. **Ejecutar el bot**, Tras comprobar que todos los pasos anteriores han sido realizados, estamos listos para ejecutar el programa.
```
$ python3 LectorMercado.py
```

## Ayuda 
Si tiene alguna duda de la función de los comandos o no sabe que comando debe ejecutar para obtener los resultados escriba dentro del chat con el bot.
```
/help
```
Esto desplegará una lista de los comandos que se encuentran activos.

## Colaboradores
<p style="text-align: center;">SaizCharly</p