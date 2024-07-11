numero = input("Ingrese un numero: ")
salida = ""
contador = 7
for n in range(0, 8):
    contador2 = contador - n
    cantidad = numero.count(str(contador2))
    salida += str(contador2)*cantidad
print(salida)    