from Console import Print, Input
import BD

def IniciarCajero():
    Print("> Iniciando Cajero Automático.")
    Print("> Ya estamos listos!")

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
    # Cambiar datos personales
        # Cambiar nombre
        # Cambiar usuario
        # Cambiar contraseña
    # Mostrar cuentas accesibles
    # Seleccionar cuenta
        # Consulta de Saldo
        # Extracción
        # Deposito

    pass
