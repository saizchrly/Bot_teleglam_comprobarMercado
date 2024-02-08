"""
Clase en la que leemos los valores de mercado de las acciones que hemos establecido.

@author: CSH
@version: 1
@date: 24/06/2023
"""
# imports
import datetime
import yfinance as yf
from src.Acciones.ListasAcciones import ListasAcciones

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
        for x in self.listaAcciones.acciones:
            nombre= x.__getitem__('nombre')
            datosAciones = yf.download(nombre, period='1d')
            if not datosAciones.empty:
                # Obtener el valor de cierre más reciente
                precioInicial = round(datosAciones['Open'].values[0], 2)
                precioFinal=round(datosAciones['Close'].values[0], 2)
                self.listaAcciones.set_valorInicial_accion(nombre,precioInicial)
                self.listaAcciones.set_valorFinal_accion(nombre,precioFinal)
                with open('./Configuracion/preciosFinales.txt', 'a') as f:
                    f.write(str(datetime.date.today()))
                    f.write(f"\n---- {x.__getitem__('nombre')} ----\n")
                    f.write('- INICIO -\n')
                    f.write(str(datosAciones['Open']))
                    f.write('\n- FIN -\n')
                    f.write(str(datosAciones['Close']))
                    f.write('\n- DIFERENCIA -\n')
                    f.write(str(self.listaAcciones.get_diferencia_accion(nombre)))
                    f.write('\n\n')