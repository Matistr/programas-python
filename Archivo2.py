from random import randint
contador = 0
with open("Ejercicios\ a.txt", "w") as archivo:
    while contador < 20:
      contador+=1
      archivo.write(str(randint(1, 100))+"\n")