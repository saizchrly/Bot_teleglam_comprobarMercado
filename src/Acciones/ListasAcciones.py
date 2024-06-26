"""
Clase creada para el control de las acciones, mediante la creación de una lista
en esta clase nos encontramos con una lista de objetos acciones, y una lista con
los nombres de dichas acciones.

A su vez encontramos las funciones correspondientes a los getter y setter correspondientes.

@author: CSH
@version: 1.3
@date: 25/05/2024
"""
from src.Acciones.Acciones import Acciones


class ListasAcciones:

    def __init__(self, accion):
        """
        Constructor.

        Args:
            accion (Array): Lista con los nombres de las acciones.
        """
        self.acciones = []
        self.nombresAcciones = []

        for x in accion:
            self.acciones.append(Acciones(x))
            self.nombresAcciones.append(x)

    def set_nueva_accion(self, accion):
        """
        Setter para una nueva acción.
        Se comprueba antes, que dicha acción no exista,
        si existe la función no hace nada,
        si no existe la función crea un nuevo objeto con la nueva acción.

        Args:
            accion (STR): Nombre de la acción nueva que vamos a introducir.
        """
        if accion not in self.nombresAcciones:
            self.acciones.append(Acciones(accion))
            self.nombresAcciones.append(accion)

    def get_valorInicial_accion(self, accion):
        """
        Obtiene el valor inicial de la acción.

        Args:
            accion (str): Nombre de la acción.

        Returns:
            int: El valor inicial de la acción. Si la acción no existe, devuelve None.
        """
        for x in self.acciones:
            if accion == x.nombreAccion:
                return x.valorInicial
        return None

    def set_valorInicial_accion(self, accion, valor):
        """
        Setter para el valor inicial de la acción.

        Args:
            accion (STR): Nombre de la acción
            valor (INT): Valor de la acción
        """
        for x in range(len(self.acciones)):
            if accion == self.acciones[x].nombreAccion:
                self.acciones[x].valorInicial = valor

    def get_valorFinal_accion(self, accion):
        """
        Obtiene el valor final de la acción.

        Args:
            accion (STR): Nombre de la acción

        Returns:
            INT: retorna el valor final, en caso de que no exista la acción no retorna nada
        """
        for x in self.acciones:
            if accion == x.nombreAccion:
                return x.valorFinal
        return None

    def set_valorFinal_accion(self, accion, valor):
        """
        Setter para el valor final de la acción.

        Args:
            accion (STR): Nombre de la acción.
            valor (INT): Valor de la acción.
        """
        for x in range(len(self.nombresAcciones)):
            if accion == self.acciones[x].nombreAccion:
                self.acciones[x].valorFinal = valor

    def get_diferencia_accion(self, accion):
        """
        Funcion que retorna el valor de la diferencia de los valores de la acción.

        Args:
            accion (STR): Nombre de la acción.

        Returns:
            INT: Diferencia entre los valores iniciales y finales de la acción.
        """
        for x in self.acciones:
            if accion == x.nombreAccion:
                return x.get_diferencia()
        return None
