
class BankAccount:
    userDni = 11222333
    saldo = 10000
    limiteExtraccion = 2000

    def __init__(self, userDni, saldo, limiteExtraccion):
        self.userDni = userDni
        self.saldo = saldo
        self.limiteExtraccion = limiteExtraccion

    def Extract(self, amount): 
        if (amount > limiteExtraccion):
            raise ValueError("No se puede extraer '%f' cuando el límite es '%f'." % (amount, self.limiteExtraccion))
        else:
            self.saldo -= amount

    def Deposit(self, amount): 
        self.saldo += amount
