
class BankAccount:
    userDni = 11222333
    saldo = 10000
    limiteExtraccion = 2000

    def Extract(self, Amount): 
        if (Amount > limiteExtraccion):
            raise ValueError("No se puede extraer '%f' cuando el límite es '%f'." % (Amount, limiteExtraccion))
        else:
            saldo -= Amount

    def Deposit(self, Amount): 
        saldo += Amount
