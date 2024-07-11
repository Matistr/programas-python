def num_distintos(lista):
    lista.sort()
    cont = 0
    for i in range(lista[-1] + 1):
        if lista.count(i) > 0:
            cont = cont +1
    return cont
lista=[1,2,3,1,2,4,1,2,3,6]
print("Salida =", num_distintos(lista))