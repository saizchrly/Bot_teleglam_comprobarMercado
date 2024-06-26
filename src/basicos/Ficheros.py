import os
import time

import os.path

    
TELEGRAM = './src/Configuracion/Bot_telegram.txt'
HELP = './src/Configuracion/Help_config.txt'
ACC = './src/Configuracion/Acciones_config.txt'
ENCRIPTADO = './src/Configuracion/Encriptado_config.txt'

# Añadir nuevas funciones para la configuración si fuese necesario
TEXTO = """\t\t### Comandos para el uso del bot ###
/start -> Este comando tiene el propósito de saber si el bot está operativo o no.
/help -> Comando usado para mostrar el menú de ayuda al usuario, el menú actual.
/reboot contraseña -> Este comando tiene el propósito de reiniciar el dispositivo donde se encuentra alojado nuestro bot.
/acciones -> Este comando mostrará las acciones que vamos a comprobar.
/accionesAdd Accion1 Accion2 -> Este comando añadirá acciones a la lista.
/accionesDel Accion1 Accion2 -> Este comando borrará acciones de la lista.
/sendAcciones -> Este comando permite mandar un documento .txt con los precios de las acciones."""

class Ficheros:

    @staticmethod
    def comprobarConfig():
        """*+
        Comprueba la configuración de los ficheros necesarios para el bot
        """
        Ficheros.desencriptadoGeneral()
        files_to_check = [TELEGRAM, HELP, ACC, ENCRIPTADO]
        for file in files_to_check:
            if not os.path.exists(file):
                open(file, 'w').close()
        if not os.path.exists(HELP):
            Ficheros.escribirFichero(TEXTO, HELP)
        if not os.path.exists(ENCRIPTADO):
            Ficheros.crearDiccionarioConfiguracion()


    @staticmethod
    def crearDiccionarioConfiguracion():
        """*+
        Crea un diccionario con los ficheros necesarios para el bot indicando si están encriptados o no
            - 1: no encriptado
            - 2: encriptado
        """
        dicionario = {'TELEGRAM': [1, TELEGRAM],
                      'HELP': [1, HELP],
                      'ACC': [1, ACC]}
        with open(ENCRIPTADO, 'w') as f:
            f.write(str(dicionario))

    @staticmethod
    def leerDiccionarioConfiguracion() -> dict:
        """*+
        Lee el diccionario de configuración de los ficheros necesarios para el bot
        
        Returns:
            dict : diccionario con los ficheros necesarios para el bot
        """
        with open(ENCRIPTADO, 'r') as f:
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
        Ficheros.descifrarArchivo(ruta)
        linea=[]
        with open(ruta, 'r') as f:
                for line in f.readlines():
                    linea.append(line.strip('\n'))
        f.close()
        Ficheros.cifrarArchivo(ruta)
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
        Ficheros.descifrarArchivo(ruta)
        acciones=[]
        texto=''
        acciones=Ficheros.leerLineas(ruta)
        Ficheros.cifrarArchivo(ruta)
        for x in acciones:
            texto += x+'\n'
        return texto

    @staticmethod
    def escribirFichero(texto:str, fichero:str, condicion:str='w'):
        """*+
        Escribe un texto en un fichero
        
        Args:
            texto (str): texto que queremos escribir
            fichero (str): fichero donde queremos escribir el texto
            condicion (str, optional): condicion para escribir el texto. Defecto a 'w'.
        """
        with open(fichero, condicion) as f:
            f.write(texto)
        f.close()
        
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
    
    @staticmethod
    def obtenerFechaCreacion(archivo: str) -> int:
        """*+
        Obtener la fecha de creación de un archivo en segundos desde la época de creacion
        y devuelve una operacion con un valor menor a 26

        Args:
            archivo (str): path del archivo que usaremos para obtener la fecha de creación

        Returns:
            int: valor de la operacion
        """
        try:
            info_archivo = os.stat(archivo)
            # Obtener la fecha de creación del archivo (en segundos desde la época)
            fecha_creacion = info_archivo.st_ctime
            anyo, mes, dia, _,_,_,_,_,_ = time.localtime(fecha_creacion)
            fecha= (anyo + mes)*dia
            valor = 1 if fecha % 26 == 0 else fecha % 26 
            return valor       
        except Exception as e:
            print (f'obtenerFechaCreacion-->\tERROR: {e}')

    @staticmethod
    def cifrarArchivo(archivo:str):
        """*+
        Cifra un archivo sumando un valor a cada caracter del archivo

        Args:
            archivo (str): archivo que queremos cifrar
        """
        valor = 1
        valor = Ficheros.obtenerFechaCreacion(archivo)
        try:
            diccionario = Ficheros.leerDiccionarioConfiguracion()
            for Key, Val in diccionario.items():
                if archivo == Val[1] and Val[0] == 1:
                    with open(archivo, 'r') as f:
                        texto_original = f.read()
                    f.close()

                    texto_cifrado = ''.join(chr(ord(c) + valor) for c in texto_original)

                    with open(archivo, 'w') as f:
                        f.write(texto_cifrado)
                    f.close()
                    Val[0] = 2
                    Ficheros.escribirFichero(str(diccionario), ENCRIPTADO)

        except Exception as e: 
            print(f'CifrarArchivo-->\tError: {e}')

    @staticmethod
    def descifrarArchivo(archivo:str):
        """*+
        Descifra un archivo restando un valor a cada caracter del archivo

        Args:
            archivo (str): archivo que queremos descifrar
        """
        valor = 1
        valor = Ficheros.obtenerFechaCreacion(archivo)
        try:
            diccionario = Ficheros.leerDiccionarioConfiguracion()
            for Key, Val in diccionario.items():
                if archivo == Val[1] and Val[0] == 2:

                    with open(archivo, 'r') as f:
                        texto_cifrado = f.read()
                    f.close()

                    texto_descifrado = ''.join(chr(ord(c) - valor) for c in texto_cifrado)

                    with open(archivo, 'w') as f:
                        f.write(texto_descifrado)
                    f.close()
                    Val[0] = 1
                    Ficheros.escribirFichero(str(diccionario), ENCRIPTADO)

        except Exception as e: 
            print(f'DescifrarArchivo-->\tError: {e}')


    @staticmethod
    def obtenerDatosArchivos (path):
        """*+
        Obtiene los datos de un archivo

        Args:
            path (str): path del archivo

        Returns:
            str: datos del archivo
        """
        try:
            Ficheros.descifrarArchivo(path)

            with open(texto, 'r') as f:
                datos = f.read()
            f.close()

            Ficheros.cifrarArchivo(path)

            return datos
        except Exception as e:
            print(f'obtenerDatosArchivos-->\tError: {e}')
            return None

    @staticmethod
    def encriptadoGeneral ():
        """*+
        Encripta todos los archivos necesarios para el bot
        """
        diccionario = Ficheros.leerDiccionarioConfiguracion()
        for key, val in diccionario.items():
            if val[0] == 1:
                diccionario[key][0] = 2
                Ficheros.cifrarArchivo(diccionario[key][1])
        Ficheros.escribirFichero(str(diccionario), ENCRIPTADO)


    @staticmethod
    def desencriptadoGeneral ():
        """*+
        Desencripta todos los archivos necesarios para el bot
        """
        diccionario = Ficheros.leerDiccionarioConfiguracion()
        for key, val in diccionario.items():
            if val[0] == 2:
                diccionario[key][0] = 1
                Ficheros.descifrarArchivo(diccionario[key][1])
        Ficheros.escribirFichero(str(diccionario), ENCRIPTADO)
