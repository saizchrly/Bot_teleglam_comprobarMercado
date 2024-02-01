import os

TELEGRAM = './Configuracion/Bot_telegram.txt'
HELP='./Configuracion/Help_config.txt'

def comprobarConfig():
    if not os.path.exists(TELEGRAM):
        open(TELEGRAM, 'w').close()
    if not os.path.exists(HELP):
        with open(HELP, 'w') as file:
            file.write('/start -> Este comando tiene el proposito de saber si el bot esta operativo o no.\n/help -> Comando usado para mostrar el menú de ayuda al usuario, el menú actual.\n/reboot contraseña -> Este comando tiene el proposito de reinicial el dispositivo donde se encuentra alojado nuesto bot\n/acciones -> Este comando mostrara las acciones que vamos a comprobar\n/acionesAdd Acion1 Acion2 -> Este comando añadirá acciones a la lista\n/acionesDel Acion1 Acion2 -> Este comando borrará acciones de la lista\n/sendAciones -> Este comandopermite mandar un documento .txt con los precios de las acciones')
        file.close()