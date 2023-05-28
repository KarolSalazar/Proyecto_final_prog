from .Caracteres import Caracter


class Letra(Caracter):
    """Clase hija que almacena instancias de letras"""
    def __init__(self, esvocal, *args, **kwargs):
        """instancias de vocales"""
        self.isvocal = esvocal
        super().__init__(self, *args, **kwargs)

    def is_vocal(self, value):
        """Verifica que el valor almacenado sea una vocal"""
        i = value
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            return True
        else:
            return False
