# Importar librerias
import src.Bot.Bot as BotC
from src.basicos.Comprobarconfiguracion import comprobarConfig, leerDiccionarioConfiguracion
from src.basicos.Encriptado import encriptadoGeneral

import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes

def main(bot):
    #obtenemos los datos del bot
    dp  = Application.builder().token(bot).build()
 
    # Asociamos manejadores para cada comando reconocible
    dp.add_handler(CommandHandler('help', BotC.help))
    dp.add_handler(CommandHandler('start', BotC.start))
    dp.add_handler(CommandHandler('reboot', BotC.reboot, has_args=True))
    dp.add_handler(CommandHandler('acciones', BotC.acciones))
    dp.add_handler(CommandHandler('accionesAdd', BotC.addAcciones, has_args=True))
    dp.add_handler(CommandHandler('accionesDel', BotC.delAcciones, has_args=True))
    dp.add_handler(CommandHandler('sendAcciones', BotC.SendAcciones))

    # Iniciamos el bot
    dp.run_polling()
    # Actualizamos el estado del bot (bloquea la ejecucion a la espera de mensajes)
    dp.idle() 
    
if __name__ == '__main__':
    comprobarConfig()
    godofredo = BotC.configuracionTelegram()
    encriptadoGeneral()
    main(godofredo)
    