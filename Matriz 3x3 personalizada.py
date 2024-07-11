matriz = []
for i in range(3):
    l = []
    for j in range(3):
        num = int(input(f"Ingrese un numero para el indice {i} {j}: "))
        l.append(num)
    matriz.append(l)    
print(matriz)