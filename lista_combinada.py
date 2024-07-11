from random import randint
Animal = ["Perro", "Gato", "Gallina", "Oveja", "Vaca", "Cerdo"]
Nombre = ["Piggy", "Nerón", "Margarita", "Manchitas", "Mimun", "Carlota"]

lista_combinada = []
while len(Animal) > 0:
    while len(Nombre) > 0:
        a = randint(0, len(Animal) - 1)
        b = randint(0, len(Nombre) - 1)
        lista_temporal = []
        lista_temporal.append(str(Animal[a]))
        lista_temporal.append(str(Nombre[b]))
        lista_combinada.append(lista_temporal)
        Animal.pop(a)
        Nombre.pop(b)

salir = 0
while salir != 1:
    print("Opcion 1: Indicar la posicion de un nombre.")
    print("Opcion 2: Indicar el tipo de mascota que tiene el nombre con más letras.")
    print("Opcion 3: Indicar el tipo de mascota a partir de su nombre.")
    print("Ingresa 0 para salir")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        nombre_mascota = input("Ingrese un nombre: ")
        for x in range(0, len(lista_combinada)):
            if lista_combinada[x][1] == nombre_mascota:
                indice = x + 1
        print(f"Posicion = {indice}")

    elif opcion == 2:
        indice = 0
        largo_nombre = len(lista_combinada[0][1])
        for x in range(0, len(lista_combinada)):
            if len(lista_combinada[x][1]) > largo_nombre:
                indice = x
        print(lista_combinada[indice][0])
                
    elif opcion == 3:
        nombre_mascota = input("Ingrese el nombre a buscar: ")
        indice = 0
        for x in range(0, len(lista_combinada)):
            if lista_combinada[x][1] == nombre_mascota:
                indice = x
        print(f"{nombre_mascota} es un(a) {lista_combinada[indice][0]}")
    elif opcion == 0:
        salir = 1
