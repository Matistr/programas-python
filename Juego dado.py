import random
class jugador():
    def __init__(self, nombre,):
        self.nombre = nombre
        self.puntaje = 0
        self.numero_lanzamientos = 0
    def __str__(self):
        return f"Jugador: {self.nombre}; puntaje: {self.puntaje}; lanzamientos: {self.numero_lanzamientos}"
    def lanzar(self):
        self.numero_lanzamientos += 1
        return random.randint(1,6)
class juego():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.puntajes_list = list([list(), list()])
        self.turn = 0
    def __str__(self):
        return f"Es el turno {self.turn} del jugador {self.p1}, es el turno {self.turn} del jugador {self.p2}"
    def iniciar_juego():
        print("Se inicia el juego")
    def jugar(self):
        if self.turno == 0:
            dado = self.jugador1.lanzar()
            self.puntajes_lista[0].append(dado)
            self.turno = 1
            self.jugador1.puntaje += dado
            print(f"Jugo el jugador 1 y obtuvo {dado} puntaje acumulado {self.jugador1.puntaje}")
        else :
            dado = self.jugador2.lanzar()
            self.puntajes_lista[1].append(dado)
            self.turno = 0
            self.jugador2.puntaje += dado
            print(f"Jugo el jugador 2 y obtuvo {dado} puntaje acumulado {self.jugador2.puntaje}")
    def juego_terminado(self):
        if (self.p1.numero_lanzamientos == 4 and self.p2.numero_lanzamientos == 4):
            return True
        elif (self.p1.puntaje == 18 and self.p2.numero_lanzamientos == 4):
            return False
    def dirimir(self):
        if self.juego_terminado() == True:
            if self.p1.puntaje > self.p2.puntaje:
                print(f"El ganador es {self.p1.nombre} con un puntaje de {self.p1.puntaje}.")
            else:
                print(f"El ganador es {self.p1.nombre} con un puntaje de {self.p1.puntaje}.")

        else:
            print("El juego no ha terminado")
    def Mostrar_rendimiento():
        pass

j1 = jugador("Mati", 0)
j2 = jugador("Lucas", 0)