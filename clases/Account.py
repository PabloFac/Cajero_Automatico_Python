
class Account:
    'Cuenta de Datos Personales de Cliente del Banco.'

    def __init__(self, id, dni, name, username, password):
        self.id = id
        self.dni = dni
        self.name = name
        self.username = username
        self.password = password

    def login(self, username, password):
        if ((self.username == username) and (self.password == password)):
            return True
        else:
            return False
