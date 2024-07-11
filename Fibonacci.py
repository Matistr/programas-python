def Fibonacci(n):
    lista = []
    lista.append(1)
    lista.append(1)
    for i in range(2, n):
        lista.append( lista[i-1] + lista[-2] )
    return lista

Fibonacci(10)