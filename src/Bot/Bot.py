import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes
from src.LectorMercado.lectorMercado import lectorMercado
from src.basicos.LlamadasSistema import LlamadasSistema
from src.basicos.Ficheros import Ficheros

TELEGRAM = './src/Configuracion/Bot_telegram.txt'
HELP='./src/Configuracion/Help_config.txt'
ACC='./src/Configuracion/Acciones_config.txt'
SEND='./src/Configuracion/preciosFinales.txt'

        
def configuracionTelegram():
    """*+
    Configuracion del emisor
    """
    linea=''
    with open(TELEGRAM, 'r') as f:
        for line in f.readlines():
            linea=str(line.strip('\n'))
    return linea
    



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
    Lineas=Ficheros.leerLineas(HELP)
    for line in Lineas:
        texto=texto+line+'\n'
       
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)

async def reboot(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
	args = context.args # ACEDEMOS A LOS ARGUMENTOS IMPORTANTE
	a = LlamadasSistema.llamadaSistemaSudo('reboot', args[0]) # Llamada al sistema con sudo
	await context.bot.send_message(chat_id=update.effective_chat.id, text='Reboot, realizado con exito.\nPara confirmar que el bot vuelve a estar operativo use /start')


async def acciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    texto = Ficheros.leerAcciones(ACC)        
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
    
async def addAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args # ACEDEMOS A LOS ARGUMENTOS IMPORTANTE
    acciones=Ficheros.leerLineas(ACC)
    with open(ACC, 'a') as f:
        for x in args:
            accion=x.upper()
            if accion not in acciones:
                f.write(accion+'\n')
    f.close()
    texto = Ficheros.leerAcciones()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='La lista de las acciones ha sido actualizada')
    
async def delAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    acciones = Ficheros.leerLineas(ACC)
    
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
    
    lectorMercado.obtener_precios_acciones(lectorMercado(Ficheros.leerLineas(ACC)))
    
    with open(SEND, 'rb') as file:
        await context.bot.send_document(chat_id=update.effective_chat.id, document=file)
    file.close()
    
    Ficheros.borrar_documento(SEND)
       
    await context.bot.send_message(chat_id=update.effective_chat.id, text='El archivo se encuentra en el mensaje anterior')
    