def encontrar_minimo(lista):
    resultado_minimo = lista[0]
    for numero in lista:
        if numero<resultado_minimo:
            resultado_minimo = numero
            
    return resultado_minimo

print(encontrar_minimo([88,12,98,3,5,7]))