import os
import subprocess

class LlamadasSistema:
    
    @staticmethod
    def llamadaSistema(entrada):
        """*+
        Hace una llamada al sistema

        Args:
            entrada (str): Comando que queremos ejecutar

        Returns:
            str: respuesta del comando ejecutado
        """
        salida = "" # Creamos variable vacia
        f = os.popen(entrada) # Llamada al sistema
        for i in f.readlines(): # Leemos caracter a caracter sobre la linea devuelta por la llamada al sistema
            salida += i  # Insertamos cada uno de los caracteres en nuestra variable
        salida = salida[:-1] # Truncamos el caracter fin de linea '\n'

        return salida # Devolvemos la respuesta al comando ejecutado

    @staticmethod
    def llamadaSistemaSudo(comando: str, contrasena):
        """*+
        Hace una llamada al sistema

        Args:
            entrada (str): Comando que queremos ejecutar
            contrasena (str): contraseña del sudo
        Returns:
            str: respuesta del comando ejecutado
        """
        Sudocomando='sudo '+ comando                
        proc = subprocess.Popen(Sudocomando, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        proc.stdin.write(contrasena.encode('utf-8'))
        proc.stdin.close()
