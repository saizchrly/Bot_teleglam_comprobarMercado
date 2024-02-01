import telegram
import os
import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes
from LectorMercado.lectorMercado import LeerPrecios
from basicos.BorarFichero import borrar_documento
from basicos.LeerDocumento import leerLineas, leerAcciones
from basicos.LlamadasSistema import llamadasSistemaSudo

TELEGRAM = './Configuracion/Bot_telegram.txt'
HELP='./Configuracion/Help_config.txt'
SUDO='./Configuracion/Sudo_config.txt'
ACC='./Configuracion/Acciones_config.txt'
SEND='./Configuracion/preciosFinales.txt'

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
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot, y estoy operativo.\nSi necesita ayuda escriba /help.")


async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    texto=''
    Lineas=leerLineas(HELP)
    for line in Lineas:
        texto=texto+line+'\n'
       
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)

async def reboot(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
	args = context.args # ACEDEMOS A LOS ARGUMENTOS IMPORTANTE
	a = llamadasSistemaSudo('reboot', args[0]) # Llamada al sistema con sudo
	await context.bot.send_message(chat_id=update.effective_chat.id, text='Reboot, realizado con exito.\nPara confirmar que el bot vuelve a estar operativo use /start')


async def acciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    texto = leerAcciones()        
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
    
async def addAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args # ACEDEMOS A LOS ARGUMENTOS IMPORTANTE
    acciones=leerLineas(ACC)
    with open(ACC, 'a') as f:
        for x in args:
            accion=x.upper()
            if accion not in acciones:
                f.write(accion+'\n')
    f.close()
    texto = leerAcciones()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='La lista de las acciones ha sido actualizada')
    
async def delAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    acciones = leerLineas(ACC)
    
    for x in range(len(args)):
        args[x]=args[x].upper()
        if args[x] in acciones:
            acciones.remove(args[x])
    
    texto=''
    with open(ACC, 'w') as f:
        for x in acciones:
            accion=x.upper()
            f.write(accion+'\n')
            texto=texto+x+'\n'
    f.close()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='La lista de las acciones ha sido actualizada')

async def SendAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    
    LeerPrecios.obtener_precios_acciones(LeerPrecios(leerLineas(ACC)))
    
    with open(SEND, 'rb') as file:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=file)
    file.close()
    
    borrar_documento(SEND)
       
    await context.bot.send_message(chat_id=update.effective_chat.id, text='El archivo se encuentra en el mensaje anterior')
    