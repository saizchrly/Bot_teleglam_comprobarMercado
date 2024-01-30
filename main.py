# Importar librerias
import Bot.Bot as BotC
from Bot.Bot import Bot

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes


def main(bot):
    args=[]
    #obtenemos los datos del bot
    dp  = Application.builder().token(bot.Token).build()
 
    # Asociamos manejadores para cada comando reconocible
    dp.add_handler(CommandHandler('help', BotC.help))
    dp.add_handler(CommandHandler('start', BotC.start))
    dp.add_handler(CommandHandler('mail', BotC.mail))
 
    # Iniciamos el bot
    dp.run_polling()
    # Actualizamos el estado del bot (bloquea la ejecucion a la espera de mensajes)
    dp.idle() 
    
if __name__ == '__main__':
    godofredo = Bot()
    godofredo.configuracionTelegram()
    main(godofredo)
    