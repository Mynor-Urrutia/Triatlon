class Nadando:
    meta = ''
    dmEquipo1 = ''  # velocidad media equipo 1
    dmEquipo2 = ''  # velocidad media equipo 2
    resultado = ''

    def __init__(self):
        print("Inicio de la Carrera de Nado")
        self.dmEquipo1 = float(input("Ingrese la distancia media de recorrido del primer equipo por hora: "))
        self.dmEquipo2 = float(input("Ingrese la distancia media de recorrido del segundo equipo por hora: "))
        self.meta = float("1")

    def Visualizacion(self):
        print("El equipo 1 tiene una velocidad media en natación es de: ", self.dmEquipo1)
        print("El equipo 2 tiene una velocidad media en natación es de: ", self.dmEquipo2)

    def Ganador(self):
        print("El equipo ganador es:")
        if self.dmEquipo1 == self.meta and self.dmEquipo2 == self.meta:
            print("Empate")
        else:
            if self.dmEquipo1 >= self.dmEquipo2:
                print("El ganador es el Equipo 1")
            else:
                print("El ganador es el equipo 2")


nada = Nadando()
nada.Visualizacion()
nada.Ganador()