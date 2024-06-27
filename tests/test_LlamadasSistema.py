import unittest
from src.basicos.LlamadasSistema import LlamadasSistema

class TestLlamadasSistema(unittest.TestCase):
    def test_llamadaSistema(self):
        entrada = "ls"
        salida = LlamadasSistema.llamadaSistema(entrada)
        self.assertIsInstance(salida, str)
        self.assertNotEqual(salida, "")

    def test_llamadaSistemaSudo(self):
        comando = "apt-get update"
        contrasena = "password"
        LlamadasSistema.llamadaSistemaSudo(comando, contrasena)
        def test_llamadaSistemaSudo(self):
            comando = "apt-get update"
            contrasena = "password"
            salida = LlamadasSistema.llamadaSistemaSudo(comando, contrasena)
            self.assertIsInstance(salida, str)
            self.assertNotEqual(salida, "")
            self.assertNotIn("Error", salida)
            self.assertIn("Reading package", salida)
            self.assertIn("Building dependency", salida)
            self.assertIn("0 upgraded", salida)

if __name__ == '__main__':
    unittest.main()