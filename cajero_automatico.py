# Proyecto: Simulador de Cajero con Python

# Librerias
import sys

# Dependencias
from Funciones import *
from Console import Println, Input, Wait

# Variables 
exitApplication = False
intentosDisponibles = 3
actualAcc = None
actualGroup = 0

# Programa
IniciarCajero()
while (exitApplication == False):
    if (actualAcc == None):
        if (intentosDisponibles > 0):
            intentosDisponibles -= 1
            actualAcc = Ingresar()
            if (actualAcc == None): 
                Println("> No se encontraron coincidencias en la base de datos.")
            else:
                Println("> Bienvenido de nuevo, %s." % (actualAcc.name))
        else:
            Println("> Ud. agotó todos sus intentos de inicio de sesión.")
            Println("> Comuniquese al 0800-000-000 para más información.")
            exitApplication = True
    else:
        MostrarOperacionesDisponibles(actualGroup)
        inputOperacion = Input("Ingrese la operacion (segun numero) a realizar: ")

        operacionRealizada = False
        for op in operaciones:
            if (op.actualGroup == actualGroup):
                if (operacionRealizada):
                    break
                if (op.keys == inputOperacion):
                    RealizarOperacion(op.id)
                    operacionRealizada = True

        if (operacionRealizada == False):
            Println("Ingresaste '%s' y no supimos que hacer :(" % (inputOperacion))
               
        if (QuiereSalir):
            Salir()
