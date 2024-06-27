import unittest
from unittest.mock import patch
from src.LectorMercado.lectorMercado import lectorMercado

class TestLectorMercado(unittest.TestCase):
    def setUp(self):
        self.acciones = ['GOOGL', 'MSFT', 'AAPL']
        self.lector = lectorMercado(self.acciones)

    def test_obtener_precios_acciones(self):
        with patch('src.LectorMercado.lectorMercado.Ficheros.escribirFichero') as mock_escribirFichero:
            with patch('src.LectorMercado.lectorMercado.yf.download') as mock_download:
                mock_download.return_value.empty = False
                mock_download.return_value['Open'].values[0] = 100.0
                mock_download.return_value['Close'].values[0] = 110.0

                self.lector.obtener_precios_acciones()

                mock_escribirFichero.assert_called_with('', './src/Configuracion/preciosFinales.txt')
                mock_download.assert_called_with('AAPL', period='1d')
                self.assertEqual(self.lector.listaAcciones.get_valorInicial_accion('AAPL'), 100.0)
                self.assertEqual(self.lector.listaAcciones.get_valorFinal_accion('AAPL'), 110.0)

    def test_obtener_precios_acciones_invalid(self):
        with patch('src.LectorMercado.lectorMercado.Ficheros.escribirFichero') as mock_escribirFichero:
            with patch('src.LectorMercado.lectorMercado.yf.download') as mock_download:
                mock_download.return_value.empty = True

                self.lector.obtener_precios_acciones()

                mock_escribirFichero.assert_called_with('La accion AAPL no existe\n', './src/Configuracion/preciosFinales.txt', 'a')

    def test_obtenerValores(self):
        datosAciones = {'Open': [100.0], 'Close': [110.0]}
        nombre = 'AAPL'

        self.lector.obtenerValores(datosAciones, nombre)

        self.assertEqual(self.lector.listaAcciones.get_valorInicial_accion('AAPL'), 100.0)
        self.assertEqual(self.lector.listaAcciones.get_valorFinal_accion('AAPL'), 110.0)

    def test_escribirAcciones(self):
        datosAciones = {'Open': [100.0], 'Close': [110.0]}
        nombre = 'AAPL'

        with patch('builtins.open', create=True) as mock_open:
            mock_file = mock_open.return_value.__enter__.return_value

            self.lector.escribirAcciones(datosAciones, nombre)

            mock_open.assert_called_with('./src/Configuracion/preciosFinales.txt', 'a')
            mock_file.write.assert_called_with(
                f"{str(datetime.date.today())}\n---- {nombre} ----\n- INICIO -\n{str(datosAciones['Open'])}\n- FIN -\n{str(datosAciones['Close'])}\n- DIFERENCIA -\n{str(self.lector.listaAcciones.get_diferencia_accion(nombre))}\n\n"
            )

if __name__ == '__main__':
    unittest.main()