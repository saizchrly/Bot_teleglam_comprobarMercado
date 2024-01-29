# Importar librerias
from telegram import CommandHandler
from telegram import MessageHandler
from telegram import Filters
from telegram import Updater

def main():
    # Crear el manejador de eventos a partir del TOKEN del bot
    updater = Updater(TOKEN)
 
    # Obtener el registro de manejadores del planificador
    dp = updater.dispatcher
 
    # Asociamos manejadores para cada comando reconocible
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ayuda", ayuda))
    dp.add_handler(CommandHandler("comandos", comandos))
    dp.add_handler(CommandHandler("apagar", apagar))
    dp.add_handler(CommandHandler("reiniciar", reiniciar))
    dp.add_handler(CommandHandler("red_conectada", red_conectada))
    dp.add_handler(CommandHandler("ip", ip))
    dp.add_handler(CommandHandler("temp", temp))
    dp.add_handler(CommandHandler("fecha", fecha))
    dp.add_handler(CommandHandler("almacenamientos", almacenamientos))
    dp.add_handler(CommandHandler("arquitectura", arquitectura))
    dp.add_handler(CommandHandler("kernel", kernel))
    dp.add_handler(CommandHandler("pwd", pwd))
    dp.add_handler(CommandHandler("drivers", drivers))
    dp.add_handler(CommandHandler("cd", cd, pass_args=True))
    dp.add_handler(CommandHandler("ls", ls, pass_args=True))
    dp.add_handler(CommandHandler("lsusb", lsusb))
    dp.add_handler(CommandHandler("montajes", montajes))
    dp.add_handler(CommandHandler("borrar", borrar, pass_args=True))
    dp.add_handler(CommandHandler("cat", cat, pass_args=True))
    dp.add_handler(CommandHandler("ssh_on", ssh_on))
    dp.add_handler(CommandHandler("ssh_off", ssh_off))
    dp.add_handler(CommandHandler("ssh_reiniciar", ssh_reiniciar))
    dp.add_handler(CommandHandler("ssh_estado", ssh_estado))
    dp.add_handler(CommandHandler("vnc_on", vnc_on))
    dp.add_handler(CommandHandler("vnc_off", vnc_off))
    dp.add_handler(CommandHandler("scriptfex", scriptfex))
    dp.add_handler(CommandHandler("exportar", exportar, pass_args=True))
    dp.add_handler(CommandHandler("importar", importar, pass_args=True))
    dp.add_handler(CommandHandler("descargar", descargar, pass_args=True))
    dp.add_handler(CommandHandler("buscar", buscar, pass_args=True))
 
    # Asociamos un manejador para cualquier mensaje recibido (no comando)
    dp.add_handler(MessageHandler(Filters.text, mensaje_nocomando))
    dp.add_handler(MessageHandler(Filters.document, archivo_recibido))
 
    # Iniciamos el bot
    updater.start_polling()
 
    # Actualizamos el estado del bot (bloquea la ejecucion a la espera de mensajes)
    updater.idle()
 
if __name__ == '__main__':
    main()