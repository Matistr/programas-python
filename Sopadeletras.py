def LeerSopaDeLetra(archivo):
    with open(archivo, "r") as archivo_sopa:
        lista_sopa = archivo_sopa.readlines()
        for indice in range(len(lista_sopa)):
            lista_sopa[indice] = lista_sopa[indice].replace("\n", "").replace(" ", "").lower()
    return lista_sopa

def EncontrarPalabra(palabra, sopa):
    for fila, linea in enumerate(sopa):
        if palabra in linea:
            print(f"SI EXISTE en la fila {fila}")
            for num_letra in range(len(linea)):
                if palabra == linea[num_letra:num_letra+len(palabra)]:
                    print(f"Columna {num_letra}")
                    return fila,num_letra

sopa_de_letras= LeerSopaDeLetra("da0Skwiy.txt")
print(sopa_de_letras)
print(EncontrarPalabra("memoria", sopa_de_letras))