
# Librerías
import sys
import time

# Configuración
animaciones = True
animacionPorCaracter = True
milisegundosEntreAnimacion = 25

def _wait():
    time.sleep(milisegundosEntreAnimacion  / 1000)
def _write(text):
    sys.stdout.write(text)
    sys.stdout.flush()


def Input(text):
    Print(text)
    return input()

def Print(text):
    if (animaciones):
        if (animacionPorCaracter):
            for char in text:
                _write(char)
                _wait()
        else:
            _write(text)
            _wait()
    else:
        _write(text)
