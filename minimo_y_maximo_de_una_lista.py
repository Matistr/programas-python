from random import *
l1 = list()
for x in range(20):
    l1.append(randint(0, 1000))
print(l1)
min = l1[0]
max = l1[0]
for elem in l1:
    if min > elem:
        min = elem
    if max < elem:
        max = elem
        
print("Minimo {min} y maximo {}".format(min,max))
