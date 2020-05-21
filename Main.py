import os
from Correr import corriendo
from Nadar import Nadando
from Pedalear import Pedaleando


def limpiarPantalla():  # Metodo para limpiar la pantalla
    print(" " * 25000000)


def pausarPantalla():  # Metodo para pausar la pantalla
    print("")
    print("\t\t\t\t\t", end="")
    os.system("pause")


class Principal():
    limpiarPantalla()
    print("Ejercicio en Python - Triatlon")
    print("Inicio del evento #1")
    carrera = corriendo()
    print("Inicio del evento #2")
    andar = Pedaleando()
    print("Inicio del evento #3")
    nada = Nadando()
    pausarPantalla()

