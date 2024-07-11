from random import randint

resp = ""
while resp != "si":
    lista =[]
    for a in range(10):
        lista.append(randint(0, 100))
        
    print(lista)
    resp = input("Esta conforme con estos numeros? ")