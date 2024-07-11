from random import randint
N = int(input("Ingrese N de la Matriz: "))
M = int(input("Ingrese M de la Matriz: "))

matriz = []
for x in range(N):
    m = []
    for z in range(M):
        m.append(randint(0, 20))
    matriz.append(m)

with open(f"Matriz_{N}_por_{M}.txt", "w") as archivo:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            archivo.write(str(matriz[i][j]))
            archivo.write(" ")
        archivo.write('\n')

with open(f"Matriz_{N}_por_{M}.txt", "r") as archivo:
    lineatxt = archivo.readlines()
    print("La matriz es la siguiente:" + "\n")
    for i in lineatxt:
        print(i)
