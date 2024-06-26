import unittest
from io import StringIO
from unittest.mock import patch
from src.Acciones.Acciones import Acciones


class TestAcciones(unittest.TestCase):
    def setUp(self):
        self.accion = Acciones("AAPL")
        self.accion.set_valor_inicial(100)
        self.accion.set_valor_final(120)

    def test___str__(self):
        expected_output = 'nombre:AAPL, valorInicial:100, valorFinal:120'
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.accion.__str__()
            self.assertEqual(fake_output.getvalue().strip(), expected_output)
        
    def test_get_nombre(self):
        self.assertEqual(self.accion.get_nombre(), "AAPL")

    def test_get_valor_inicial(self):
        self.assertEqual(self.accion.get_valor_inicial(), 100)

    def test_get_valor_final(self):
        self.assertEqual(self.accion.get_valor_final(), 120)

    def test_get_diferencia(self):
        self.assertEqual(self.accion.get_diferencia(), 20)
        
    def test_set_nombre(self):
        self.accion.set_nombre("KO")
        self.assertEqual(self.accion.get_nombre(), "KO")

    def test_set_valor_inicial(self):
        self.accion.set_valor_inicial(150)
        self.assertEqual(self.accion.get_valor_inicial(), 150)

    def test_set_valor_final(self):
        self.accion.set_valor_final(200)
        self.assertEqual(self.accion.get_valor_final(), 200)
    
        


if __name__ == '__main__':
    unittest.main()