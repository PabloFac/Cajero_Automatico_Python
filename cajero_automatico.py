# Proyecto: Cajero Automático

# Librerias
import sys

# Librerias Internas
import Console
import Operaciones

# Programa
Console.Print("Bienvenido/a al cajero automático.")

contrasena = input("\nIngrese su contraseña: ")
contrasena = int(contrasena)

intentos_c = 0 #intentos de la clave
intentos_n = 0 #intentos del nombre

while contrasena > 0:
    if contrasena != clave:
        Console.Print("\nError al ingresar la contraseña.")
        contrasena = input("\nReingrese su contraseña: ")
        contrasena = int(contrasena)
        intentos_c = intentos_c + 1
        if intentos_c > 1:
            Console.Print("\nYa no puede volver a ingresar su contraseña, agotó los 3 (tres) intentos, comuníquese al 0800-000-000.")
            Console.Print("\nGracias por utilizar el cajero. Que tenga buenos días.")
            sys.exit() #funcion para terminar un programa
    else:
        break

nombre_usuario = input("\nIngrese su nombre de usuario: ")

while nombre_usuario != " ":
    if nombre_usuario != usuario:
        Console.Print("\nError al ingresar su nombre de usuario.")
        nombre_usuario = input("\nReingrese su nombre de usuario, recuerde respetar mayúsculas: ")
        intentos_n = intentos_n + 1
        if intentos_n > 1:
            Console.Print("\nYa no puede volver a ingresar su usuario, agotó los 3 (tres) intentos, comuníquese al 0800-000-000.")
            Console.Print("\nGracias por utilizar el cajero. Que tenga buenos días.")
            sys.exit() #funcion para terminar un programa
    else:
        break

Console.Print("\nHas accedido con éxito, Bienvenido/a: ", nombre_usuario)
Console.Print("\nMenú: ")
Console.Print("\n1- Consultar saldo.")
Console.Print("\n2- Extracciones.")
Console.Print("\n3- Depósito.")
Console.Print("\n4- Cambiar límite de extracción.")
Console.Print("\n5- Cambiar contraseña.")

opcion = input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
opcion = int(opcion)

while opcion > 0:
    if opcion < 0 or opcion > 5:
        Console.Print("Error al ingresar la opción.")
        Console.Print("La opción ingresada no existe.")
        opcion = input("Reingrese el número de opción: ")
        opcion = int(opcion)
    else:
        break

if opcion == 1:
    Console.Print("\nUsted eligió la opción CONSULTAR SALDO.")
    Console.Print("\nSu saldo actual es: $", saldo)
    seguir = input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
    if seguir == "S":
        opcion = input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
        opcion = int(opcion)
        if opcion == 2:
            Console.Print("\nUsted eligió la opción EXTRACCIONES.")
            extraer = input("\nIngrese el monto a extraer: ")
            extraer = int(extraer)
            while extraer > 0:
                if extraer > limite_ex:
                    Console.Print("\nEl monto ingresado excede su límite de extracción.")
                    extraer = input("\nReingrese el monto a extraer: ")
                    extraer = int(extraer)
                else:
                    Console.Print("\nUsted extrajo $", extraer, "de su saldo.")
                    Console.Print("\nSu saldo actual es: $", Operaciones.Extraccion(saldo, extraer))
                    saldo_actual = Operaciones.Extraccion(saldo, extraer)
                    saldo = saldo_actual
                    seguir = input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
                    if seguir == "S":
                        opcion = input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
                        opcion = int(opcion)
                        if opcion == 3:
                            Console.Print("\nUsted eligió la opcion DEPÓSITO.")
                            deposito = input("\nIngrese la cantidad de dinero que desea depositar: ")
                            deposito = int(deposito)
                            while  deposito > 0:
                                if deposito < 1:
                                    Console.Print("\nIngrese una cantidad positiva de dinero.")
                                    deposito = input("\nReingrese la cantidad de dinero a depositar: ")
                                    deposito = int(deposito)
                                else:
                                    Console.Print("\nUsted depositó $", deposito, ".")
                                    Console.Print("\nSu saldo actual es: ", Operaciones.Deposito(saldo_actual, deposito))

                                    seguir = input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
                                    if seguir == "S":
                                        opcion = input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
                                        opcion = int(opcion)
                                        if opcion == 4:
                                            Console.Print("\nUsted eligió CAMBIAR LÍMITE DE EXTRACCIÓN.")
                                            cambio_lim = input("\nIngrese el nuevo límite: ")
                                            cambio_lim = int(cambio_lim)
                                            Console.Print("\nSu límite anterior de", limite_ex, "ahora es de: ", cambio_lim)
                                            limite_ex = cambio_lim
                                            seguir = input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
                                            if seguir == "S":
                                                opcion = input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
                                                opcion = int(opcion)
                                                if opcion == 5:
                                                    Console.Print("\nUsted eligió CAMBIO DE CONTRASEÑA.")
                                                    verifica = input("\nIngrese su contraseña anterior: ")
                                                    verifica = int(verifica)
                                                    while verifica != clave:
                                                        Console.Print("\nContraseña antigua incorrecta.")
                                                        verifica = input("\nReingrese su contraseña anterior: ")
                                                        verifica = int(verifica)
                                                        if verifica == clave:
                                                            clave_nueva = input("\nIngrese su clave nueva: ")
                                                            Console.Print("\nSu nueva clave ha sido generada.")
                                                            seguir = input("\n¿Desea hacer otra consulta? S/N: ") #mayúsculas
                                                            if seguir == "S":
                                                                opcion = input("\nIngrese el número de la opción que requiera (1, 2, 3, 4, 5): ")
                                                                opcion = int(opcion)
                                                            else:
                                                                Console.Print("\nGracias por utilizar el cajero. Que tenga un buen día.")
                                                                sys.exit()	
                                    else:
                                        Console.Print("\nGracias por utilizar el cajero. Que tenga un buen día.")
                                        sys.exit()

                    else:
                        Console.Print("\nGracias por utilizar el cajero. Que tenga un buen día.")
                        sys.exit()
    else:
        Console.Print("\nGracias por utilizar el cajero. Que tenga un buen día.")
        sys.exit()