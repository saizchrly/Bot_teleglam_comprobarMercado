import unittest
from src.Acciones.ListasAcciones import ListasAcciones

class TestListasAcciones(unittest.TestCase):
    def setUp(self):
        acciones = ["AAPL", "KO", "GOOGL"]
        self.lista_acciones = ListasAcciones(acciones)

    def test_set_nueva_accion(self):
        self.lista_acciones.set_nueva_accion("TSLA")
        self.assertIn("TSLA", self.lista_acciones.nombresAcciones)

    def test_get_valorInicial_accion(self):
        # Exisiten las acciones
        # Expected: 0
        valor_inicial = self.lista_acciones.get_valorInicial_accion("AAPL")
        self.assertEqual(valor_inicial, 0)
        valor_inicial = self.lista_acciones.get_valorInicial_accion("KO")
        self.assertEqual(valor_inicial, 0)
        valor_inicial = self.lista_acciones.get_valorInicial_accion("GOOGL")
        self.assertEqual(valor_inicial, 0)
        
        # No existe la accion de la accion NO_EXISTE
        # Expected: None
        valor_inicial = self.lista_acciones.get_valorInicial_accion("NO_EXISTE")
        self.assertEqual(valor_inicial, None)

    def test_set_valorInicial_accion(self):
        self.lista_acciones.set_valorInicial_accion("AAPL", 100)
        valor_inicial = self.lista_acciones.get_valorInicial_accion("AAPL")
        self.assertEqual(valor_inicial, 100)

    def test_get_valorFinal_accion(self):
        # Expected: 0
        valor_final = self.lista_acciones.get_valorFinal_accion("KO")
        self.assertEqual(valor_final, 0)
        
        # Expected: None
        valor_final = self.lista_acciones.get_valorFinal_accion("NO_EXISTE")
        self.assertEqual(valor_final, None)

    def test_set_valorFinal_accion(self):
        self.lista_acciones.set_valorFinal_accion("KO", 200)
        valor_final = self.lista_acciones.get_valorFinal_accion("KO")
        self.assertEqual(valor_final, 200)

    def test_get_diferencia_accion(self):
        # Expected: 0
        diferencia = self.lista_acciones.get_diferencia_accion("GOOGL")
        self.assertEqual(diferencia, 0)
        
        #Prueba con valores
        self.lista_acciones.set_valorInicial_accion("GOOGL", 100)
        self.lista_acciones.set_valorFinal_accion("GOOGL", 200)
        # Expected: 100
        diferencia = self.lista_acciones.get_diferencia_accion("GOOGL")
        self.assertEqual(diferencia, 100)
        
        # Expected: None
        valor_final = self.lista_acciones.get_valorFinal_accion("NO_EXISTE")
        self.assertEqual(valor_final, None)


if __name__ == '__main__':
    unittest.main()