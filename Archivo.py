contador = 0

with open("cien.txt", "w") as archivo:
    while contador < 100:
        contador+=1
        archivo.write(str(contador)+"\n")
        
print(archivo)