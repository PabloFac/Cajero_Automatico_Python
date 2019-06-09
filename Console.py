
# Librerías
import sys
import time

# Configuración
animaciones = True
animacionPorCaracter = True
milisegundosEntreAnimacion = 50

# Funciones Privadas
def __write(text):
    sys.stdout.write(text)
    sys.stdout.flush()
def _waitForAnim():
    Wait(milisegundosEntreAnimacion)

# Funciones Publicas
def Wait(x):
    time.sleep(x  / 1000)

def Input():
    return input()

def Input(text):
    Print(text)
    return input()

def Print(text):
    if (animaciones):
        if (animacionPorCaracter):
            for char in text:
                __write(char)
                Wait()
        else:
            __write(text)
            Wait()
    else:
        __write(text)

def Println(text):
    Print(text + "\n")
