
class Account:   
    dni = 11222333
    name = "Admin"
    username = "admin"
    password = "admin"

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
