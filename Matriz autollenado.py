from random import randint

m = []
for i in range(5):
  l = []
  for j in range(5):
    l.append(randint(0,1000))
  m.append(l)

id_i = int(input("Ingrese un indice para las filas: "))
id_j = int(input("Ingrese un indice para las columnas: "))
valor = input("ingrese un valor: ")

m[id_i][id_j] = valor
print(m)