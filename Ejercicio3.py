def num_distintos(lista):
    lista.sort()
    nueva = {}
    for i in range(lista[-1] + 1):
        if lista.count(i) > 0:
            nueva[i]=lista.count(i)
    last=list(nueva.values())
    last.sort(reverse=True)
    mayor = last[0]
    ok_lista = list(nueva.items())
    for i in ok_lista:
        if i[1] == mayor:
            veces = i[1]
            repetido = i[0]
    resultado = str(repetido) + ", " + str(veces) + f"  El más repetido es el {repetido} y se repite {veces} veces."
    return resultado
lista = [1, 2, 3, 1, 2, 4, 1, 2, 3, 6, 1]
print(num_distintos(lista))