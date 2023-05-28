
class Caracter:
    def __init__(self, value, isletter):
        self.value = value
        self.isletter = isletter

    def verificar_letra(self, value):
        if value.isalnum() and not value.isdigit():
            return True
        else:
            return False
