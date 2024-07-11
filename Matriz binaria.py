matriz = [[0, 1, 0],
       [1, 0, 1],
       [0, 1, 0]]
print(matriz)
for indice_i in range(len(matriz)):
    for indice_j in range(len(matriz[indice_i])):
        matriz[indice_i][indice_j] = 1 if matriz[indice_i][indice_j]==0 else 0
print(matriz)