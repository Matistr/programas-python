def filtrador_pares(lista):
    lista_p = []
    for i in lista:
        if i % 2 == 0:
            lista_p.append(i)
    return lista_p
def filtrador_impares(lista):
    lista_i = []
    for i in lista:
        if i % 2 != 0:
            lista_i.append(i)
    return lista_i
def suma_lista(lista):
    s = sum(lista)
    return s
def serie(x,y):
    listaxy = []
    listaxy.append(x+y)
    listaxy.append((x+y)+y)
    for i in range(2, (x+y)):
        listaxy.append(listaxy[i-1] + listaxy[i-2])
    return listaxy[-1]
def sumador_digitos(z):
    suma = 0
    for d in str(z):
        suma += int(d)
    return suma
lista = [1, 4, 3, 2]
#lista_p = filtrador_pares(lista)
#lista_i = filtrador_impares(lista)
#print(lista_p)
#print(lista_i)
#print(suma_lista(lista))
#x = suma_lista(lista_i)
#y = suma_lista(lista_p)
#s = serie(x,y)
#print(x)
#print(y)
#print(s)

print(sumador_digitos(serie(suma_lista(filtrador_pares(lista)), suma_lista(filtrador_impares(lista)))))