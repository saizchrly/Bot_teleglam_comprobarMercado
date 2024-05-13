from src.basicos.Encriptado import descifrarArchivo, cifrarArchivo

def leerLineas(ruta):
    """*+
    Leer las lineas de un documento proporcionado mediante ruta

    Args:
        ruta (str): ruta del documento

    Returns:
        LIST: lista de las lineas del documento
    """
    descifrarArchivo(ruta)
    linea=[]
    with open(ruta, 'r') as f:
            for line in f.readlines():
                linea.append(line.strip('\n'))
    f.close()
    cifrarArchivo(ruta)
    return linea


def leerAcciones(ruta: str):
    """*+
    Lee las lineas de un documento y las incorpora a una variable tipo str

    Args:
        ruta (str): direccion del cocumento

    Returns:
        srt: String de las lineas del documento
    """
    descifrarArchivo(ruta)
    acciones=[]
    texto=''
    acciones=leerLineas(ruta)
    cifrarArchivo(ruta)
    for x in acciones:
        texto=texto+x+'\n'
    return texto