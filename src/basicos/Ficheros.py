import os
from src.basicos.Encriptado import Encriptado

class Ficheros:
    
    TELEGRAM = './src/Configuracion/Bot_telegram.txt'
    HELP = './src/Configuracion/Help_config.txt'
    ACC = './src/Configuracion/Acciones_config.txt'
    ENCRIPTADO = './src/Configuracion/Encriptado_config.txt'

    # Añadir nuevas funciones para la configuración si fuese necesario
    TEXTO = """\t\t\t### Comandos para el uso del bot ###
    /start -> Este comando tiene el propósito de saber si el bot está operativo o no.
    /help -> Comando usado para mostrar el menú de ayuda al usuario, el menú actual.
    /reboot contraseña -> Este comando tiene el propósito de reiniciar el dispositivo donde se encuentra alojado nuestro bot.
    /acciones -> Este comando mostrará las acciones que vamos a comprobar.
    /accionesAdd Accion1 Accion2 -> Este comando añadirá acciones a la lista.
    /accionesDel Accion1 Accion2 -> Este comando borrará acciones de la lista.
    /sendAcciones -> Este comando permite mandar un documento .txt con los precios de las acciones."""

    @staticmethod
    def comprobarConfig():
        """*+
        Comprueba la configuración de los ficheros necesarios para el bot
        """
        Encriptado.desencriptadoGeneral()
        files_to_check = [Ficheros.TELEGRAM, Ficheros.HELP, Ficheros.ACC, Ficheros.ENCRIPTADO]
        for file in files_to_check:
            if not os.path.exists(file):
                open(file, 'w').close()
        if not os.path.exists(Ficheros.HELP):
            Ficheros.escribirFichero(Ficheros.TEXTO, Ficheros.HELP)
        if not os.path.exists(Ficheros.ENCRIPTADO):
            Ficheros.crearDiccionarioConfiguracion()


    @staticmethod
    def crearDiccionarioConfiguracion():
        """*+
        Crea un diccionario con los ficheros necesarios para el bot indicando si están encriptados o no
            - 1: no encriptado
            - 2: encriptado
        """
        dicionario = {'TELEGRAM': [1, Ficheros.TELEGRAM],
                      'HELP': [1, Ficheros.HELP],
                      'ACC': [1, Ficheros.ACC]}
        with open(Ficheros.ENCRIPTADO, 'w') as f:
            f.write(str(dicionario))

    @staticmethod
    def leerDiccionarioConfiguracion() -> dict:
        """*+
        Lee el diccionario de configuración de los ficheros necesarios para el bot
        
        Returns:
            dict : diccionario con los ficheros necesarios para el bot
        """
        with open(Ficheros.ENCRIPTADO, 'r') as f:
            diccionario = eval(f.read())
        return diccionario
    
    @staticmethod
    def leerLineas(ruta):
        """*+
        Leer las lineas de un documento proporcionado mediante ruta

        Args:
            ruta (str): ruta del documento

        Returns:
            LIST: lista de las lineas del documento
        """
        Encriptado.descifrarArchivo(ruta)
        linea=[]
        with open(ruta, 'r') as f:
                for line in f.readlines():
                    linea.append(line.strip('\n'))
        f.close()
        Encriptado.cifrarArchivo(ruta)
        return linea

    @staticmethod
    def leerAcciones(ruta: str):
        """*+
        Lee las lineas de un documento y las incorpora a una variable tipo str

        Args:
            ruta (str): direccion del cocumento

        Returns:
            srt: String de las lineas del documento
        """
        Encriptado.descifrarArchivo(ruta)
        acciones=[]
        texto=''
        acciones=leerLineas(ruta)
        Encriptado.cifrarArchivo(ruta)
        for x in acciones:
            texto += x+'\n'
        return texto

    @staticmethod
    def escribirFichero(texto:str, fichero:str):
        """*+
        Escribe un texto en un fichero
        
        Args:
            texto (str): texto que queremos escribir
            fichero (str): fichero donde queremos escribir el texto
        """
        with open(fichero, 'w') as f:
            f.write(texto)
    
    @staticmethod
    def borrar_documento(ruta):
        """*+
        Borra el fichero una vez se ha mandado

        Args:
            ruta (STR): ruta donde se encuentra el fichero a borrar
        """
        if os.path.exists(ruta):
            os.remove(ruta)
            print("El documento ha sido borrado exitosamente.")
        else:
            print("El documento no existe.")   