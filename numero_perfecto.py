def numero_perfecto(a):
    suma = 0
    for divisor in range(1, a - 1):
        if (a % divisor) == 0:
            suma += divisor
    if suma != a:
        return False
    elif suma == a:
        return True

x = int(input("Ingrese un numero: "))
print(numero_perfecto(x))