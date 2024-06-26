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
        
        # diferencia entre el valor final y el valor inicial
        self.diferencia = 0
    
    def __str__(self):
        """*+
        Transforma a string los datos del objeto.
        """
        print('\nnombre:{}, valorInicial:{}, valorFinal:{}'.format(
            self.nombreAccion, self.valorInicial, self.valorFinal, ))
    
    def get_nombre(self):
        """
        Getter del nombre de la acción

        Returns:
            STR: Nombre de la acción
        """
        return self.nombreAccion

    def get_valor_inicial(self):
        """
        Getter del valor inicial

        Returns:
            INT: Valor inicial
        """
        return self.valorInicial

    def get_valor_final(self):
        """
        Getter del valor final

        Returns:
            INT: Valor final
        """
        return self.valorFinal
    
    def get_diferencia(self):
        """
        Getter de la diferencia entre el valor final y el valor inicial

        Returns:
            INT: Diferencia entre el valor final y el valor inicial
        """
        self.diferencia = self.calcular_diferencia()
        return self.diferencia

    def set_nombre(self, nombre):
        """
        Setter del nombre de la acción

        Args:
            nombre (STR): Nuevo nombre de la acción
        """
        self.nombreAccion = nombre

    def set_valor_inicial(self, valor):
        """
        Setter del valor inicial

        Args:
            valor (INT): Nuevo valor inicial
        """
        self.valorInicial = valor

    def set_valor_final(self, valor):
        """
        Setter del valor final

        Args:
            valor (INT): Nuevo valor final
        """
        self.valorFinal = valor
    

    def set_diferencia(self, valor):
        """
        Setter de la diferencia entre el valor final y el valor inicial

        Returns:
            INT: Diferencia entre el valor final y el valor inicial
        """
        self.diferencia = valor

    def calcular_diferencia(self):
        """
        Calcula la diferencia entre el valor final y el valor inicial

        Returns:
            INT: Diferencia entre el valor final y el valor inicial
        """
        return self.valorFinal - self.valorInicial 