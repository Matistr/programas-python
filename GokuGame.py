from tkinter import N


def GokuGame(matriz, personaje, fila, columna):
    if matriz[fila][columna] == 0 or matriz[fila][columna] == "0":
        matriz[fila][columna] = personaje[0]
        return True
    else:
        return False
def Campo_de_batalla(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()
def SaveGame(matriz):
    with open("Game.txt", "w") as archivo:
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                archivo.write(str(matriz[i][j]))
            archivo.write('\n')
def LoadGame():
    with open("Game.txt", "r") as archivo:
        lineatxt = archivo.readline()
        for i in range(0, 6):
            for j in range(0, 6):
                matriz[i][j] = lineatxt[j]
            lineatxt = archivo.readline()
def buscar_personaje(personaje, mapa):
    for i in range(mapa):
        for j in range(len(mapa)):
            if mapa[i][j] == personaje:
                return i,j
    return False            
def mover_arriba(matriz):
    posx, posy = buscar_personaje("G", matriz)
    newx = posx - 1
    if newx < 0 or newx >= len(matriz) or matriz[newx][posy] == 1:
        print("No se puede mover a esa posicion")
    else:
        matriz[posx][posy] = "*"
        matriz[newx][posy] = "G"
def mover_abajo(matriz):
    posx, posy = buscar_personaje("G", matriz)
    newx = posx + 1
    if newx < 0 or newx >= len(matriz) or matriz[newx][posy] == 1:
        print("No se puede mover a esa posicion")
    else:
        matriz[posx][posy] = "*"
        matriz[newx][posy] = "G"
def mover_izquierda(matriz):
    posx, posy = buscar_personaje("G", matriz)
    newy = posy - 1
    if newy < 0 or newy >= len(matriz) or matriz[newy][posy] == 1:
        print("No se puede mover a esa posicion")
    else:
        matriz[posx][posy] = "*"
        matriz[posx][newy] = "G"
def mover_derecha(matriz):
    posx, posy = buscar_personaje("G", matriz)
    newy = posy + 1
    if newy < 0 or newy >= len(matriz) or matriz[newy][posy] == 1:
        print("No se puede mover a esa posicion")
    else:
        matriz[posx][posy] = "*"
        matriz[posx][newy] = "G"
matriz = [[0,0,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,1,0],[0,1,0,0,1,0],[0,1,0,1,1,0],[0,1,0,0,0,0]]
LoadGame()
salir = 0
while salir != 1:
    personaje = "G" #input("Ingrese nombre del personaje: ")
    fila = int(input("Ingrese coordenada de fila: "))
    columna = int(input("Ingrese coordenada de columna: "))
    funciono = GokuGame(matriz, personaje, fila, columna)
    if funciono:
        print("¡Personaje ingresado con éxito!")
    else:
        print("No se puede ingresar el personaje ahí, ya que no está disponible.")
    Campo_de_batalla(matriz)
SaveGame(matriz)

while movimiento != 0:
    movimiento = input("Ingrese movimiento (wasd o 0 salir)")
    if movimiento == w:
        mover_arriba(matriz)
    elif movimiento == a:
        mover_izquierda(matriz)
    elif movimiento == s:
        mover_abajo(matriz)
    elif movimiento == d:
        mover_derecha(matriz)
    print(Campo_de_batalla(matriz))