
from Console import Println, Input, Wait
from clases.Operacion import Operacion
import BD

import sys

operaciones = [
    Operacion(0, 0, 100, "0", "Salir"),
    Operacion(0, 0, 102, "1", "Mostrar Cuentas asociadas"),
    Operacion(1, 1, 201, "2", "Cambiar Nombre completo"),
    Operacion(1, 1, 202, "3", "Cambiar Usuario"),
    Operacion(1, 1, 203, "4", "Cambiar Contraseña"),
    Operacion(1, 2, 301, "5", "Consulta de Saldo"),
    Operacion(1, 2, 302, "6", "Extracción"),
    Operacion(1, 2, 303, "7", "Deposito"),
]


def IniciarCajero():
    Println("> Iniciando Cajero Automático.")
    Println("> Ya estamos listos!")
    Println("> Acceso por defecto: admin, admin")

def Ingresar():
    logged = False
    while (logged == False):
        # Pedir datos al usuario:
        usuario = Input("< Usuario: ")
        contraseña = Input("< Contraseña: ")
        # Comprobar en base de datos
        for acc in BD.accounts:
            if (acc.login(usuario, contraseña)):                
                return acc
                break
        else:
            return None

def MostrarOperacionesDisponibles():
    for op in operaciones:
        Println(str(op))

def Salir():
    Println("> Gracias por utilizar este cajero.")
    Println("> Le deseamos lo mejor!")
    Wait(3000)
    sys.exit()

def RealizarOperacion(id):
    if (id == "100"):
        Salir()

        pass
    elif (id == "102"):

        pass