from .Caracteres import Caracter


class Especial(Caracter):
    def __init__(self, isnum, *args, **kwargs):
        self.isnum = isnum
        super().__init__(self, *args, **kwargs)

    def is_num(self, value):
        i = value
        if i.isdigit():
            return True
        else:
            return False
