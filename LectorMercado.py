# Importar librerias
from src.Bot.Bot import Bot
from src.basicos.Ficheros import Ficheros

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes

def main(bot):
    #obtenemos los datos del bot
    dp  = Application.builder().token(bot.get_bot()).build()
 
    # Asociamos manejadores para cada comando reconocible
    dp.add_handler(CommandHandler('help', Bot.help))
    dp.add_handler(CommandHandler('start', Bot.start))
    dp.add_handler(CommandHandler('reboot', Bot.reboot, has_args=True))
    dp.add_handler(CommandHandler('acciones', Bot.acciones))
    dp.add_handler(CommandHandler('accionesAdd', Bot.addAcciones, has_args=True))
    dp.add_handler(CommandHandler('accionesDel', Bot.delAcciones, has_args=True))
    dp.add_handler(CommandHandler('sendAcciones', Bot.SendAcciones))

    # Iniciamos el bot
    dp.run_polling()
    # Actualizamos el estado del bot (bloquea la ejecucion a la espera de mensajes)
    dp.idle() 
    
if __name__ == '__main__':
    Ficheros.comprobarConfig()
    godofredo = Bot()
    Ficheros.encriptadoGeneral()
    main(godofredo)