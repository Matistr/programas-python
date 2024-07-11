t = int(input("Ingrese el instante de tiempo t:"))
vf = 20
v0 = 10
a = (vf-v0)/t
x = v0 * t + ((a * (t*t)) /2)
print("La aceleración de la partícula es:" + str(a) , "y la posición es:" + str(x))
