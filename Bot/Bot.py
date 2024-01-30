import telegram
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes

TELEGRAM = './Configuracion/Bot_telegram.txt'
HELP='./Configuracion/Help_config.txt'

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
    print(1)
    salida = "" # Creamos variable vacia
    f = os.popen(entrada) # Llamada al sistema
    for i in f.readlines(): # Leemos caracter a caracter sobre la linea devuelta por la llamada al sistema
        salida += i  # Insertamos cada uno de los caracteres en nuestra variable
    salida = salida[:-1] # Truncamos el caracter fin de linea '\n'

    return salida # Devolvemos la respuesta al comando ejecutado


async def ls(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE,):
	
	_ls = llamadaSistema("ls") # Llamada al sistema
	await context.bot.send_message(chat_id=update.effective_chat.id, text=_ls)