import os
from .src.basicos.Encriptado import cifrarArchivo

TELEGRAM = './src/Configuracion/Bot_telegram.txt'
HELP='./src/Configuracion/Help_config.txt'
ACC='./src/Configuracion/Acciones_config.txt'

def comprobarConfig():
    if not os.path.exists(TELEGRAM):
        open(TELEGRAM, 'w').close()
    if not os.path.exists(HELP):
        with open(HELP, 'w') as file:
            file.write('/start -> Este comando tiene el proposito de saber si el bot esta operativo o no.\n/help -> Comando usado para mostrar el menú de ayuda al usuario, el menú actual.\n/reboot contraseña -> Este comando tiene el proposito de reinicial el dispositivo donde se encuentra alojado nuesto bot\n/acciones -> Este comando mostrara las acciones que vamos a comprobar\n/accionesAdd Acion1 Acion2 -> Este comando añadirá acciones a la lista\n/accionesDel Acion1 Acion2 -> Este comando borrará acciones de la lista\n/sendAcciones -> Este comandopermite mandar un documento .txt con los precios de las acciones')
        file.close()
    if not os.path.exists(ACC):
        open(ACC, 'w').close()
    
    cifrarArchivo(TELEGRAM)
    cifrarArchivo(HELP)
    cifrarArchivo(ACC)