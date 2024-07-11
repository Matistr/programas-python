from random import randint
insertados = []
m = []
for _ in range(5):
  l = []
  for _ in range(5):
    aleatorio = randint(0,24)
    while aleatorio in insertados:
      aleatorio = randint(0,24)
    l.append(aleatorio)
    insertados.append(aleatorio)
  m.append(l)
print(m)