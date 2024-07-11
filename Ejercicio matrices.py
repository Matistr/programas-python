##Ejercicio 1
# def funcion(matriz):
#     for i in range(len(matriz)):
#         for j in range(len(matriz[i])):
#             matriz[i][j] = matriz[i][j]**2
#     print(matriz)

# matriz = [[1,1,1,1,1], [0,0,0,0,0], [3,3,3,3,3], [0,0,0,0,0], [2,2,2,2,2]]
# funcion(matriz)
# print(matriz)

##Ejercicio 2
def RotarMatriz90(matriz):
    rotada = []
    for i in range(len(matriz)):
        m2 = list()
        for j in range(len(matriz[i])):
            m2.append(0)
        rotada.append(m2)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            rotada[j][len(matriz) - 1 - i] = matriz[i][j]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] = rotada[i][j]

def RotarMatriz180(matriz):
    RotarMatriz90(matriz)
    RotarMatriz90(matriz)

def RotarMatriz270(matriz):    
    RotarMatriz90(matriz)
    RotarMatriz90(matriz)
    RotarMatriz90(matriz)

from random import randint
m = []
for i in range(9):
  l = []
  for j in range(9):
    l.append(randint(0,9))
  m.append(l)

print(m)
rotar = int(input("Ingrese los grados en los que desea voltear la matriz (90, 180, 270): "))
if rotar == 90:
    print(RotarMatriz90(m))
elif rotar == 180:
    print(RotarMatriz180(m))
elif rotar == 270:
    print(RotarMatriz270(m))