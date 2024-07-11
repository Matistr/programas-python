from random import randint
n = int(input("Ingrese la cantidad de numeros aleatorios"))
lista = [randint(0, 100) for _ in range(n)]
print(lista)
while lista.count(0) != len(lista):
    min = 99999
    for elem in lista:
        if min> and elem>0:
            min = elem
    print(min)        
for i in range(len(lista)):
    if lista[i] > 0:
        lista[i] = lista[i] - min
        print(lista)