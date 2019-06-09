from Console import Println, Input
from clases.Operacion import Operacion
import BD

operaciones = [
    Operacion(0, "1", "Cambiar datos personales"),
    Operacion(0, "2", "Mostrar Cuentas asociadas"),
    Operacion(0, "3", "Seleccionar Cuenta"),
    Operacion(1, "1", "Cambiar Nombre completo"),
    Operacion(1, "2", "Cambiar Usuario"),
    Operacion(1, "3", "Cambiar Contraseña"),
    Operacion(1, "1", "Consulta de Saldo"),
    Operacion(1, "2", "Extracción"),
    Operacion(1, "3", "Deposito"),
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
        if (op.identLevel == 0):
            Println(str(op))
