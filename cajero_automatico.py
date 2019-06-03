# Proyecto: Simulador de Cajero con Python

# Librerias
import sys

# Dependencias
from Console import Print, Input
from Funciones import *

# Variables 
exitApplication = False
intentosDisponibles = 5
actualAcc = None

# Configuracion
Console.animaciones = True    
Console.animacionPorCaracter = True
Console.milisegundosEntreAnimacion = 10

# Programa
IniciarCajero()
while (exitApplication == False):
    if (actualAcc == None):
        if (intentosDisponibles > 0):
            intentosDisponibles -= 1
            actualAcc = Ingresar()
            if (actualAcc == None): 
                Print("> No se encontraron coincidencias en la base de datos.")
            else:
                Print("> Bienvenido de nuevo, %s." % (actualAcc.name))
        else:
            Print("> Ud. agotó todos sus intentos de inicio de sesión.")
            Print("> Comuniquese al 0800-000-000 para más información.")
    else:
        # Mostrar operaciones disponibles
        # Preguntar sobre operacion a realizar
        # Realizar operacion
        # preguntar si salir
        # quiere salir:
            # saludar
            # esperar x seg.
            # salir
            # borrar pantalla
        # no quiere salir:
            # empezar de nuevo
        pass

Print("> Que tenga buenos días.")
sys.exit()