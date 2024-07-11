with open("Ejercicios\ a.txt", "r") as archivo:
  resultados = archivo.readlines()
suma = 0
for n in resultados:
        suma += int(n)
        
print(suma)
