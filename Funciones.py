
from Console import Println, Input, Wait
from clases.Operacion import Operacion
import BD

import sys

operaciones = [
    Operacion(100, "0", "Salir"),
    Operacion(101, "1", "Mostrar Cuentas asociadas"),
    Operacion(102, "2", "Cambiar Nombre completo"),
    Operacion(103, "3", "Cambiar Usuario"),
    Operacion(104, "4", "Cambiar Contraseña"),
    Operacion(105, "5", "Consulta de Saldo"),
    Operacion(106, "6", "Extracción"),
    Operacion(107, "7", "Deposito"),
]

def RealizarOperacion(id, accId):
    if (id == 100):
        Salir()
    elif (id == 101):
        MostrarCuentasAsociadas(accId)
    elif (id == 102):
        CambiarNombreCompleto(accId)
    elif (id == 103):
        CambiarUsuario(accId)
    elif (id == 104):
        CambiarContraseña(accId)
    elif (id == 105):
        ConsultaSaldo(accId)



def ConsultaSaldo():
    bkAccId = Input("< Ingrese el Nro de Cuenta: ")
    for bkAcc in BD.bankAccounts:
        if ((bkAcc.id == bkAccId) and (bkAccId )):

    bkAcc = Input("< Ingrese el Nro de Cuenta: ")



def CambiarContraseña(accId):
    newPass1 = Input("< Ingrese un nueva contraseña: ")
    newPass2 = Input("< Confirme la nueva contraseña: ")
    if (newPass1 == newPass2):
        for acc in BD.accounts:
            if (acc.id == accId):
                acc.password = newPass1
                break
        Println("> Contraseña actualizada con éxito.")
    else:
        Println("> Las contraseñas no coinciden.")

def CambiarUsuario(accId):
    newUser = Input("< Ingrese un nuevo usuario: ")
    for acc in BD.accounts:
        if (acc.id == accId):
            acc.usuario = newUser
            break
    Println("> Usuario actualizado con éxito.")

def CambiarNombreCompleto(accId):
    newName = Input("< Ingrese un nuevo nombre: ")
    for acc in BD.accounts:
        if (acc.id == accId):
            acc.name = newName
            break
    Println("> Nombre actualizado con éxito.")

def MostrarCuentasAsociadas(accId):
    Println("> Cuentas asociadas: ")
    for bkAcc in BD.bankAccounts:
        if (bkAcc.userId == accId):
            Println("- %s" % (bkAcc.id))

def GetAccountName(accId):
    for acc in BD.accounts:
        if (acc.id == accId):
            return acc.name

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
