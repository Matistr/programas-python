def Convertir(cadena):
    lista_salida = []
    for caracter in cadena:
        lista_salida.append(ord(caracter))
    return lista_salida

Convertir("abcde")
