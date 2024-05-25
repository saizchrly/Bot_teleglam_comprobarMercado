import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes
from src.LectorMercado.lectorMercado import lectorMercado
from src.basicos.Ficheros import Ficheros
from src.basicos.LlamadasSistema import LlamadasSistema

TELEGRAM = './src/Configuracion/Bot_telegram.txt'
HELP='./src/Configuracion/Help_config.txt'
ACC='./src/Configuracion/Acciones_config.txt'
SEND='./src/Configuracion/preciosFinales.txt'

class Bot:
    
    def __init__(self):
        """*+
        Constructor de la clase Bot, en el que se inicializa el bot de telegram
        """
        self.set_bot(TELEGRAM)

    def set_bot(self, path: str):
        """*+
        Funcion set_bot, en la que se inicializa el bot de telegram

        Args:
            path (str): ruta del fichero donde se encuentra el token del bot
        """
        self.bot =Ficheros.leerLineas(path)[0]
                
    def get_bot(self) -> str:
        """*+
        Funcion get_bot, en la que se devuelve el bot de telegram

        Returns:
            str : token del bot
        """
        return self.bot
        
    @staticmethod
    async def start(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion start, con la que comprobaremos que el bot se encuentra operativo

        Args:
            update (telegram.Update): constructor del bot
            context (ContextTypes.DEFAULT_TYPE): tipo de contexto
        """
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Soy un bot, y estoy operativo.\nSi necesita ayuda escriba /help.")

    @staticmethod
    async def help(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion help, con la que se muestra la ayuda del bot

        Args:
            update (telegram.Update): update del bot
            context (ContextTypes.DEFAULT_TYPE): contexto del bot
        """
        texto = ''
        Lineas = Ficheros.leerLineas(HELP)
        for line in Lineas:
            texto = texto + line + '\n'

        await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)

    @staticmethod
    async def reboot(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion reboot, con la que se reinicia el bot

        Args:
            update (telegram.Update): update del bot
            context (ContextTypes.DEFAULT_TYPE): contexto del bot
        """
        args = context.args  # ACEDEMOS A LOS ARGUMENTOS IMPORTANTE
        a = LlamadasSistema.llamadaSistemaSudo('reboot', args[0])  # Llamada al sistema con sudo
        await context.bot.send_message(chat_id=update.effective_chat.id, text='Reboot, realizado con exito.\nPara confirmar que el bot vuelve a estar operativo use /start')

    @staticmethod
    async def acciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion acciones, con la que se muestran las acciones que se van a comprobar

        Args:
            update (telegram.Update): update del bot
            context (ContextTypes.DEFAULT_TYPE): contexto del bot
        """
        texto = Ficheros.leerAcciones(ACC)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)

    @staticmethod
    async def addAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion addAcciones, con la que se añaden acciones a la lista de acciones a comprobar

        Args:
            update (telegram.Update): update del bot
            context (ContextTypes.DEFAULT_TYPE): contexto del bot
        """
        args = context.args  # ACEDEMOS A LOS ARGUMENTOS IMPORTANTE
        acciones = Ficheros.leerLineas(ACC)
        
        for x in args:
            accion = x.upper()
            if accion not in acciones:
                acciones.append(accion)
        
        Ficheros.escribirFichero(acciones, ACC)
        texto = Ficheros.leerAcciones()
        await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='La lista de las acciones ha sido actualizada')

    @staticmethod
    async def delAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion delAcciones, con la que se eliminan acciones de la lista de acciones a comprobar

        Args:
            update (telegram.Update): update del bot
            context (ContextTypes.DEFAULT_TYPE): contexto del bot
        """
        args = context.args
        acciones = Ficheros.leerLineas(ACC)

        for x in args:
            accion = x.upper()
            if accion in acciones:
                acciones.remove(accion)

        Ficheros.escribirFichero(acciones, ACC)
        texto = Ficheros.leerAcciones(ACC)
    
        await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)
        await context.bot.send_message(chat_id=update.effective_chat.id, text='La lista de las acciones ha sido actualizada')

    @staticmethod
    async def SendAcciones(update: telegram.Update, context: ContextTypes.DEFAULT_TYPE):
        """*+
        Funcion SendAcciones, con la que se envian las acciones a comprobar

        Args:
            update (telegram.Update): update del bot
            context (ContextTypes.DEFAULT_TYPE): contexto del bot
        """
        lectorMercado.obtener_precios_acciones(lectorMercado(Ficheros.leerLineas(ACC)))

        with open(SEND, 'rb') as file:
            await context.bot.send_document(chat_id=update.effective_chat.id, document=file)
        file.close()

        Ficheros.borrar_documento(SEND)

        await context.bot.send_message(chat_id=update.effective_chat.id, text='El archivo se encuentra en el mensaje anterior')
