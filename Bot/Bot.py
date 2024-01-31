import telegram
import os
import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes

TELEGRAM = './Configuracion/Bot_telegram.txt'
HELP='./Configuracion/Help_config.txt'
SUDO='./Configuracion/Sudo_config.txt'
ACC='./Configuracion/Acciones_config.txt'

class Bot:
    """*+
    Creacion del objeto Bot
    """
    def __init__(self):
        """Constructor del objeto.
        """
        self.Token = ""
        self.id = ""
    def __str__(self):
        print('El token es: ' + str(self.Token) + '\n' + 'El id es: '+str(self.Id))
        
    def configuracionTelegram(self):
        """*+
        Configuracion del emisor
        """
        lineas = []
        with open(TELEGRAM, 'r') as f:
            for line in f.readlines():
                lineas.append(line.strip('\n'))
        self.Token = lineas[0]
        self.id = lineas[1]



async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    """*+
    Funcion start, con la que comprobaremos que el bot se encuentra operativo

    Args:
        update (telegram.Update): constructor del bot
        context (ContextTypes.DEFAULT_TYPE): tipo de contexto
    """
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot, y estoy operativo.")


async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    
    
    await context.bot.send_message(chat_id=update.effective_chat.id, text='WIP')

def llamadaSistema(entrada):
    salida = "" # Creamos variable vacia
    f = os.popen(entrada) # Llamada al sistema
    for i in f.readlines(): # Leemos caracter a caracter sobre la linea devuelta por la llamada al sistema
        salida += i  # Insertamos cada uno de los caracteres en nuestra variable
    salida = salida[:-1] # Truncamos el caracter fin de linea '\n'

    return salida # Devolvemos la respuesta al comando ejecutado

def llamadasSistemaSudo(comando: str):
    Sudocomando='sudo '+ comando
    contrasena= ''
    with open(SUDO, 'r') as f:
            for line in f.readlines():
                contrasena=line.strip('\n')
                
    proc = subprocess.Popen(Sudocomando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    proc.stdin.write(contrasena.encode('utf-8'))
    proc.stdin.close()

async def reboot(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE,):
	
	a = llamadasSistemaSudo('reboot') # Llamada al sistema con sudo
	await context.bot.send_message(chat_id=update.effective_chat.id, text='Reboot, realizado con exito.\nPara confirmar que el bot vuelve a estar operativo use /start')

def leerLineas(ruta):
    linea=[]
    with open(ruta, 'r') as f:
            for line in f.readlines():
                linea.append(line.strip('\n'))
    return linea

async def acciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    acciones=[]
    texto=''
    acciones=leerLineas(ACC)
    
    for x in acciones:
        texto=x+'\n'
        
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)