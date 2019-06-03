
# Librerías
import sys
import time

# Configuración
animaciones = True
animacionPorCaracter = True
milisegundosEntreAnimacion = 25

# Funciones Privadas
def __wait():
    time.sleep(milisegundosEntreAnimacion  / 1000)
def __write(text):
    sys.stdout.write(text)
    sys.stdout.flush()

# Funciones Publicas
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
                __wait()
        else:
            __write(text)
            __wait()
    else:
        __write(text)
