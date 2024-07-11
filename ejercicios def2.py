def suma_diagonal(matriz):
    suma = 0
    for i in range(0, 5):
        suma = suma + matriz[i][i]
    return print(f"La suma de la diagonal de esta matriz es de: {suma}")
def suma_diagonal_inversa(matriz):
    suma = 0
    for x in range(0,5):
        suma += matriz[x][4-x]
    return print(f"La suma de la diagonal inversa de esta matriz es de: {suma}")
def matriz_triangular(matriz):
    for i in range(0,5):
        if matriz[]
        pass
matriz = [[1,4,2,5,6],[0,1,4,8,-1],[0,0,1,4,3],[0,0,0,1,3],[0,0,0,0,1]]
suma_diagonal(matriz)
suma_diagonal_inversa(matriz)