import unittest
from unittest.mock import patch, mock_open
from src.basicos.Ficheros import Ficheros

class TestFicheros(unittest.TestCase):
    def setUp(self):
        self.ficheros = Ficheros()

    def test_comprobarConfig(self):
        contenido_mock = "{'TELEGRAM': [1, './src/Configuracion/Bot_telegram.txt'], 'HELP': [1, './src/Configuracion/Help_config.txt'], 'ACC': [1, './src/Configuracion/Acciones_config.txt']}"  # Asegúrate de que este contenido sea el esperado por tu función
        with patch('builtins.open', mock_open(read_data=contenido_mock)) as mocked_open:
            self.ficheros.comprobarConfig()
            mocked_open.assert_called_with('./src/Configuracion/Encriptado_config.txt', 'w')


    def test_crearDiccionarioConfiguracion(self):
        with patch('builtins.open') as mock_open:
            self.ficheros.crearDiccionarioConfiguracion()
            mock_open.assert_called_with('./src/Configuracion/Encriptado_config.txt', 'w')

    def test_leerDiccionarioConfiguracion(self):
        with patch('builtins.open') as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = "{'TELEGRAM': [1, './src/Configuracion/Bot_telegram.txt'], 'HELP': [1, './src/Configuracion/Help_config.txt'], 'ACC': [1, './src/Configuracion/Acciones_config.txt']}"
            diccionario = self.ficheros.leerDiccionarioConfiguracion()
            self.assertEqual(diccionario, {'TELEGRAM': [1, './src/Configuracion/Bot_telegram.txt'], 'HELP': [1, './src/Configuracion/Help_config.txt'], 'ACC': [1, './src/Configuracion/Acciones_config.txt']})

    def test_leerLineas(self):
        with patch('builtins.open') as mock_open:
            mock_open.return_value.__enter__.return_value.readlines.return_value = ['line1\n', 'line2\n', 'line3\n']
            lineas = self.ficheros.leerLineas('./src/Configuracion/Bot_telegram.txt')
            self.assertEqual(lineas, ['line1', 'line2', 'line3'])

    def test_leerAcciones(self):
        with patch('builtins.open') as mock_open:
            mock_open.return_value.__enter__.return_value.readlines.return_value = ['AAPL\n', 'GOOGL\n', 'TSLA\n']
            acciones = self.ficheros.leerAcciones('./src/Configuracion/Acciones_config.txt')
            self.assertEqual(acciones, 'AAPL\nGOOGL\nTSLA\n')

    def test_escribirFichero_Bot(self):
        with patch('builtins.open') as mock_open:
            self.ficheros.escribirFichero('texto', './src/Configuracion/Bot_telegram.txt', 'w')
            mock_open.assert_called_with('./src/Configuracion/Bot_telegram.txt', 'w')
    
    def test_escribirFichero_help(self):
        with patch('builtins.open') as mock_open:
            self.ficheros.escribirFichero('texto', './src/Configuracion/Help_config.txt', 'w')
            mock_open.assert_called_with('./src/Configuracion/Help_config.txt', 'w')

    def test_borrar_documento(self):
        with patch('os.path.exists') as mock_exists, patch('os.remove') as mock_remove:
            mock_exists.return_value = True
            self.ficheros.borrar_documento('./src/Configuracion/Bot_telegram.txt')
            mock_remove.assert_called_with('./src/Configuracion/Bot_telegram.txt')

    def test_obtenerFechaCreacion(self):
        with patch('os.stat') as mock_stat, patch('time.localtime') as mock_localtime:
            mock_stat.return_value.st_ctime = 1638472800
            mock_localtime.return_value = (2021, 12, 3, 0, 0, 0, 0, 0, 0)
            
            #calculo de los valores que saca la función
            valor_que_debe_dar = (2021 + 12)*3
            valor_que_debe_dar = 1 if valor_que_debe_dar % 26 == 0 else valor_que_debe_dar % 26
            
            try:
                valor_retornado = self.ficheros.obtenerFechaCreacion('./src/Configuracion/Bot_telegram.txt')
                self.assertEqual(valor_retornado, valor_que_debe_dar)
            except Exception as e:
                self.fail(f"Raised an exception: {e}")

    def test_cifrarArchivo(self):
        with patch('builtins.open') as mock_open, patch('src.basicos.Ficheros.Ficheros.obtenerFechaCreacion') as mock_fecha:
            mock_fecha.return_value = 3
            self.ficheros.cifrarArchivo('./src/Configuracion/Bot_telegram.txt')
            mock_open.assert_called_with('./src/Configuracion/Encriptado_config.txt', 'r')

    def test_descifrarArchivo(self):
        with patch('builtins.open') as mock_open, patch('src.basicos.Ficheros.Ficheros.obtenerFechaCreacion') as mock_fecha:
            mock_fecha.return_value = 3
            self.ficheros.descifrarArchivo('./src/Configuracion/Bot_telegram.txt')
            mock_open.assert_called_with('./src/Configuracion/Encriptado_config.txt', 'r')

    def test_obtenerDatosArchivos(self):
        with patch('builtins.open') as mock_open, patch('src.basicos.Ficheros.Ficheros.descifrarArchivo'), patch('src.basicos.Ficheros.Ficheros.cifrarArchivo'):
            mock_open.return_value.__enter__.return_value.read.return_value = 'datos'
            datos = self.ficheros.obtenerDatosArchivos('./src/Configuracion/Bot_telegram.txt')
            self.assertEqual(datos, 'datos')
            
    def test_encriptadoGeneral(self):
        with patch('src.basicos.Ficheros.Ficheros.leerDiccionarioConfiguracion') as mock_leer, patch('src.basicos.Ficheros.Ficheros.cifrarArchivo') as mock_cifrar, patch('src.basicos.Ficheros.Ficheros.escribirFichero') as mock_escribir:
            mock_leer.return_value = {'TELEGRAM': [1, './src/Configuracion/Bot_telegram.txt'], 'HELP': [1, './src/Configuracion/Help_config.txt'], 'ACC': [1, './src/Configuracion/Acciones_config.txt']}
            self.ficheros.encriptadoGeneral()
            mock_cifrar.assert_called_with('./src/Configuracion/Acciones_config.txt')
            mock_escribir.assert_called_with("{'TELEGRAM': [2, './src/Configuracion/Bot_telegram.txt'], 'HELP': [2, './src/Configuracion/Help_config.txt'], 'ACC': [2, './src/Configuracion/Acciones_config.txt']}", './src/Configuracion/Encriptado_config.txt')    
    
    def test_desencriptadoGeneral(self):
        with patch('src.basicos.Ficheros.Ficheros.leerDiccionarioConfiguracion') as mock_leer, patch('src.basicos.Ficheros.Ficheros.descifrarArchivo') as mock_descifrar, patch('src.basicos.Ficheros.Ficheros.escribirFichero') as mock_escribir:
            mock_leer.return_value = {'TELEGRAM': [2, './src/Configuracion/Bot_telegram.txt'], 'HELP': [2, './src/Configuracion/Help_config.txt'], 'ACC': [2, './src/Configuracion/Acciones_config.txt']}
            self.ficheros.desencriptadoGeneral()
            mock_descifrar.assert_called_with('./src/Configuracion/Acciones_config.txt')
            mock_escribir.assert_called_with("{'TELEGRAM': [1, './src/Configuracion/Bot_telegram.txt'], 'HELP': [1, './src/Configuracion/Help_config.txt'], 'ACC': [1, './src/Configuracion/Acciones_config.txt']}", './src/Configuracion/Encriptado_config.txt')

if __name__ == '__main__':
    unittest.main()
