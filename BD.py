# Clases utilizadas por BD
from clases.Account import Account
from clases.BankAccount import BankAccount 

# Base de datos (Arrays)
accounts = []
bankAccounts = []

# Carga de Base de Datos
accounts.append(Account(1001, 11222333, "Admin", "admin", "admin"))
bankAccounts.append(BankAccount(1153, 11222333, 10000, 2500))
