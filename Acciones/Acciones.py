"""
Clase Acciones, genera un objeto acción, el dual posee el nombre de la acción,
el valor y los datos iniciales, y el valor y los datos finales.

A su vez tenemos los geter, y seter de los datos del objeto, junto con una funcion
que se encarga de calcular el valance de la acción.

@autor:CSH
@version: 2
@date: 24/06/2023

"""


class Acciones:

    def __init__(self, nombreAccion):
        """*+
        Constructor

        Args:
            nombreAccion (STR): Nombre de la acción para la creacion del objeto.
        """
        # nombre de la acción
        self.nombreAccion = nombreAccion
        # valor inicial
        self.valorInicial = 0

        # valor final
        self.valorFinal = 0
        
        self.diferencia = self.valorFinal-self.valorInicial

    def __getitem__(self, indice):
        """*+
        Geters del objeto

        Args:
            indice (STR): Indice para la devolución de los datos del objeto

        Returns:
            Depende el indice devuelve lo que corresponde
        """
        if indice == 'nombre':
            return self.nombreAccion
        elif indice == 'valorInicial':
            return self.valorInicial
        elif indice == 'valorFinal':
            return self.valorFinal

    def __str__(self):
        """*+
        Transforma a string los datos del objeto.
        """
        print('\nnombre:{}, valorInicial:{}, valorFinal:{}'.format(
            self.nombreAccion, self.valorInicial, self.valorFinal, ))

    def __setitem__(self, indice, valor):
        """*+
        Setter del objeto acciones.

        Args:
            indice (STR): Dato del objeto que se quiere modificar
            valor (STR, INT): Valor nuevo que se quiere dar a ese objeto
        """
        if indice == 'nombre':
            self.nombreAccion = valor
        elif indice == 'valorInicial':
            self.valorInicial = valor
        elif indice == 'valorFinal':
            self.valorFinal = valor

