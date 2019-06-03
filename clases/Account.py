
class Account:
    'Cuenta de Datos Personales de Cliente del Banco.'

    def __init__(self, dni, name, username, password):
        self.dni = dni
        self.name = name
        self.username = username
        self.password = password

    def login(self, username, password):
        if ((self.username == username) and (self.password == password)):
            return True
        else:
            return False
