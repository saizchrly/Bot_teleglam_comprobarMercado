# Importar librerias
from src.Bot.Bot import Bot
from src.basicos.Ficheros import Ficheros

    
if __name__ == '__main__':
    Ficheros.comprobarConfig()
    godofredo = Bot()
    Ficheros.encriptadoGeneral()
    Bot.start_bot(godofredo)