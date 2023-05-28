
class Caracter:
    """Clase principal que almacena instancias de Caracteres"""
    def __init__(self, value, isletter):
        """Se define la clase Caracter"""
        self.value = value
        self.isletter = isletter

    def verificar_letra(self, value):
        """Clase que verifica si el caracter es una letra o no"""
        if value.isalnum() and not value.isdigit():
            return True
        else:
            return False
