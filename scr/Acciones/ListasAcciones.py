"""
Clase creada para el control de las acciónes, mediante la creación de una lista
en esta clase nos encontramos con una lista de objetos acciónes, y una lista con
los nombres de dichas acciónes.

A su vez encontramos las funciones correspondientes a los getter y setter correspondientes.

@author: CSH
@version: 1.2
@date: 24/06/2023
"""
# imports
from Acciones.Acciones import Acciones


class ListasAcciones:

    def __init__(self, accion):
        """*+
        Constructor.

        Args:
            acción (Array): Lista con los nombres de las acciónes.
        """
        self.acciones = []
        self.nombresAcciones = []

        for x in accion:
            self.acciones.append(Acciones(x))
            self.nombresAcciones.append(x)

    def set_nueva_accion(self, accion):
        """*+
        Setter para una nueva acción.
        Se comprueba antes, que dicha acción no exisita, 
        si exisite la funcion no hace nada, 
        si no existe la funcion crea un nuevo objeto con la nueva acción.

        Args:
            acción (STR): Nombre de la acción nueva que vamos a introducir.
        """
        if accion not in self.nombresAcciones:
            self.acciones.append(Acciones(accion))
            self.nombresAcciones.append(accion)

    def get_valorInicial_accion(self, accion):
        """*+
        Obtienes el valor inicial de la acción.

        Args:
            acción (STR): Nombre de la acción

        Returns:
            INT: retorna el valor inicial, en caso de que no exista la acción no retorna nada
        """
        if accion in self.nombresAcciones:
            for x in self.acciones:
                if accion == x.__getitem__('nombre'):
                    return x.__getitem__('valorInicial')

    def set_valorInicial_accion(self, accion, valor):
        """*+
        Setter para el valor inicial de la acción.

        Args:
            acción (STR): Nombre de la acción
            valor (INT): Valor de la acción
        """
        for x in range(len(self.acciones)):
            if accion == self.acciones[x].__getitem__('nombre'):
                self.acciones[x].__setitem__('valorInicial', valor)
                
    def get_valorFinal_accion(self, accion):
        """*+
        Obtienes el valor final de la acción.

        Args:
            acción (STR): Nombre de la acción

        Returns:
            INT: retorna el valor final, en caso de que no exista la acción no retorna nada
        """
        if accion in self.nombresAcciones:
            for x in self.acciones:
                if accion == x.__getitem__('nombre'):
                    return x.__getitem__('valorFinal')

    def set_valorFinal_accion(self, accion, valor):
        """*+
        Setter para el valor final de la acción.

        Args:
            acción (STR): Nombre de la acción.
            valor (INT): Valor de la acción.
        """
        for x in range(len(self.nombresAcciones)):
            if accion == self.acciones[x].__getitem__('nombre'):
                self.acciones[x].__setitem__('valorFinal', valor)
                
    def get_diferencia_accion(self, accion):
        """*+
        Funcion que retorna el valor de la diferencia de los valores de la acción.

        Args:
            accion (STR): Nombre de la acción.

        Returns:
            INT: Diferencia entre los valores iniciales y finales de la acción.
        """
        for x in self.acciones:
            if accion == x.__getitem__('nombre'):
                return x.diferencia
