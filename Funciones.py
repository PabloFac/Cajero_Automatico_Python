from Console import Println, Input
from clases.Operacion import Operacion
import BD

operaciones = [
    Operacion(0, 0, 100, "1", "Cambiar datos personales"),
    Operacion(0, 0, 101, "2", "Mostrar Cuentas asociadas"),
    Operacion(0, 0, 102, "3", "Seleccionar Cuenta"),
    Operacion(1, 1, 201, "1", "Cambiar Nombre completo"),
    Operacion(1, 1, 202, "2", "Cambiar Usuario"),
    Operacion(1, 1, 203, "3", "Cambiar Contraseña"),
    Operacion(1, 2, 301, "1", "Consulta de Saldo"),
    Operacion(1, 2, 302, "2", "Extracción"),
    Operacion(1, 2, 303, "3", "Deposito"),
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

def MostrarOperacionesDisponibles(group):
    for op in operaciones:
        if (op.group == group):
            Println(str(op))



def QuiereSalir():
    entrada = Input("> Ingrese 'exit' sin comillas para salir del Cajero Automático: ")
    if (entrada == "exit"):
        return True
    else:
        return False

def Salir():
    Println("> Gracias por utilizar este cajero.")
    Println("> Le deseamos lo mejor!")
    Wait(3000)
    sys.exit()

def RealizarOperacion(id):
    if (id == "1"):

        pass
    elif (id == "1"):

        pass