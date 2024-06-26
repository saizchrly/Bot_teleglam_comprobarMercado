"""
Clase en la que leemos los valores de mercado de las acciones que hemos establecido.

@author: CSH
@version: 1.2
@date: 25/05/2024
"""
# imports
import datetime
import yfinance as yf
from src.Acciones.ListasAcciones import ListasAcciones
from src.basicos.Ficheros import Ficheros

SEND='./src/Configuracion/preciosFinales.txt'
class lectorMercado:
    
    def __init__(self, acciones):
        """*+
        Construrtor
        Args:
            acciones (List): Lista de las accones que queremos consultar
        """
        self.listaAcciones = ListasAcciones(acciones)
        
    def obtener_precios_acciones(self):
        """*+
        Funcion utilizada para la lectura de los valores de mercado de las acciones.
        Args:
            condicion (INT): Esta condcion indica si los valores a leer son de por la mañana o de por la tarde
        """
        Ficheros.escribirFichero('', SEND)
        
        for x in self.listaAcciones.acciones:
            
            nombre= x.get_nombre()
            datosAccion = yf.download(nombre, period='1d')
            if not datosAccion.empty:
                
                valorInicial = round (datosAccion['Open'].values[0] ,2)
                valorFinal = round ( datosAccion['Close'].values[0] ,2)
                
                self.listaAcciones.set_valorInicial_accion(nombre,valorInicial)
                self.listaAcciones.set_valorFinal_accion(nombre,valorFinal)
                
                self.escribirAcciones(datosAccion, nombre)     
            else:
                Ficheros.escribirFichero(f"La accion {nombre} no existe\n", SEND, 'a')
    
    def escribirAcciones(self, datosAciones, nombre):
        """*+
        Funcion utilizada para la escritura de las acciones en un fichero
        """
        with open(SEND, 'a') as f:
            f.write(str(datetime.date.today()))
            f.write(f"\n---- {nombre} ----\n")
            f.write('- INICIO -\n')
            f.write(str(datosAciones['Open']))
            f.write('\n- FIN -\n')
            f.write(str(datosAciones['Close']))
            f.write('\n- DIFERENCIA -\n')
            f.write(str(self.listaAcciones.get_diferencia_accion(nombre)))
            f.write('\n\n')
        f.close()