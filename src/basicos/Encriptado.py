import os.path
import time

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

def cifrarArchivo(archivo:str):
    """*+
    Cifra un archivo sumando un valor a cada caracter del archivo

    Args:
        archivo (str): archivo que queremos cifrar
    """
    valor = 1
    valor = obtenerFechaCreacion(archivo)
    try:
        with open(archivo, 'r') as f:
            texto_original = f.read()
        f.close()

        texto_cifrado = ''.join(chr(ord(c) + valor) for c in texto_original)

        with open(archivo, 'w') as f:
            f.write(texto_cifrado)
        f.close()
        
    except Exception as e: 
        print(f'CifrarArchivo-->\tError: {e}')

def descifrarArchivo(archivo:str):
    """*+
    Descifra un archivo restando un valor a cada caracter del archivo

    Args:
        archivo (str): archivo que queremos descifrar
    """
    valor = 1
    valor = obtenerFechaCreacion(archivo)
    try:
        with open(archivo, 'r') as f:
            texto_cifrado = f.read()
        f.close()

        texto_descifrado = ''.join(chr(ord(c) - valor) for c in texto_cifrado)

        with open(archivo, 'w') as f:
            f.write(texto_descifrado)
        f.close()
        
    except Exception as e: 
        print(f'DescifrarArchivo-->\tError: {e}')

