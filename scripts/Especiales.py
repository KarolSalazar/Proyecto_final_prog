from .Caracteres import Caracter


class Especial(Caracter):
    """Clase hija que almacena instancias de Caracteres especiales"""
    def __init__(self, isnum, *args, **kwargs):
        """Ser inicializa caracter especial"""
        self.isnum = isnum
        super().__init__(self, *args, **kwargs)

    def is_num(self, value):
        """Se verifica si es un número o no"""
        i = value
        if i.isdigit():
            return True
        else:
            return False
