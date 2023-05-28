from .Caracteres import Caracter


class Letra(Caracter):
    def __init__(self, esvocal, *args, **kwargs):
        self.isvocal = esvocal
        super().__init__(self, *args, **kwargs)

    def is_vocal(self, value):
        i = value
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            return True
        else:
            return False
