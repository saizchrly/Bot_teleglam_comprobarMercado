# Bot Lector de Mercado
Este es un bot de Telegram, desarrollado por el momento para ejecutarse en máquinas Linux, enfocado en la lectura de los datos de las acciones que el usuario ha introducido con anterioridad.
Está desarrollado principalmente con la librería *python-telegram-bot*, aunque se apoya en otras librerías para la ejecución de los comandos, como la librería *yfinance*, para la obtención de los datos de las acciones en el mercado

## Método de ejecución
1. Primero de todo debes tener en el equipo docker, Siya posees docker en tu equipo puedes saltar el paso 2
Si no lo tienes puedes descargarlo de dos formas, la version grafica, [link](https://www.docker.com/products/docker-desktop/), o si deseas descargarlo por linea de comandos en linux.

- Seguir los comandos en orden
```
sudo apt update
```
```
sudo apt install apt-transport-https ca-certificates curl software-properties-common
```
```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
```
```
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
```
```
sudo apt update
```
```
sudo apt install docker-ce
```
- Si no deseas escribir sudo cadáver que necesites ejecutar un comando de Docker escribe lo siguiente, este paso es opcional.
Cambie 'USER' por su usuario
```
sudo usermod -aG docker ${USER}
```
```
su - ${USER}
```
- Compruebe que su usuario se encuentra en la lista con el siguiente comando
```
id -nG
```


## Ayuda 
Si tiene alguna duda de la función de los comandos o no sabe que comando debe ejecutar para obtener los resultados escriba dentro del chat con el bot.
```
/help
```
Esto desplegará una lista de los comandos que se encuentran activos.

## Colaboradores
<p style="text-align: center;">SaizCharly</p