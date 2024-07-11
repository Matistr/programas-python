tablero = [['o', 'x', 'o'], ['x', 'o', 'x'], ['-', 'x', 'o']]
#print(tablero)
for i in range(len(tablero)):
    if tablero[i][0] == tablero[i][1] and tablero[i][0] == tablero[i][2]:
        print("El tablero está terminado")
    if tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]:
        print("El tablero está terminado")
    if tablero[0][i] == tablero[0][i+1] and tablero[0][i] == tablero[0][i+2]:
        print("El tablero está terminado")




print("El tablero aún no está terminado...")