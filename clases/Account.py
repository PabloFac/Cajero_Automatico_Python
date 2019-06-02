
class Account:   
    dni = 11222333
    name = "Admin"
    username = "admin"
    password = "admin"

    def login(self, Username, Password):

        if ((username == Username) and (password == Password)):
            return True
        else:
            return False
