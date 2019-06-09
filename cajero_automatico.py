# Proyecto: Simulador de Cajero con Python


# Dependencias
from Funciones import *
from Console import Println, Input, Wait

# Variables 
accId = None
exitApplication = False
intentosDisponibles = 3

# Programa
IniciarCajero()
while (exitApplication == False):
    if (accId == None):
        if (intentosDisponibles > 0):
            intentosDisponibles -= 1
            accIdaccId = Ingresar()
            if (accId == None): 
                Println("> No se encontraron coincidencias en la base de datos.")
            else:
                Println("> Bienvenido de nuevo, %s." % GetAccountName(accId))
        else:
            Println("> Ud. agotó todos sus intentos de inicio de sesión.")
            Println("> Comuniquese al 0800-000-000 para más información.")
            exitApplication = True
    else:
        MostrarOperacionesDisponibles()
        inputOperacion = Input("Ingrese la operacion (segun numero) a realizar: ")

        operacionRealizada = False
        for op in operaciones:
            if (op.keys == inputOperacion):
                RealizarOperacion(op.id, accId)
                operacionRealizada = True
                break 

        if (operacionRealizada == False):
            Println("Ingresaste '%s' y no supimos que hacer :(" % (inputOperacion))
               
