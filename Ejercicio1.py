def cuantos_son_primos(lista):
    contador = 0
    for numero in range(len(lista)):
        indice = 2
        primo = True
        while indice < lista[numero]:
            resto = lista[numero] % indice
            if resto == 0:
                primo = False
            indice = indice + 1    
        if primo and (lista[numero] != 1):
                contador = contador + 1      
    return contador            
lista = [1,7,8,5,13]
print("Se encontraron", cuantos_son_primos(lista), "numeros primos")