def borrar_documento(ruta):
        """*+
        Borra el fichero una vez se ha mandado

        Args:
            ruta (STR): ruta donde se encuentra el fichero a borrar
        """
        if os.path.exists(ruta):
            os.remove(ruta)
            print("El documento ha sido borrado exitosamente.")
        else:
            print("El documento no existe.")   