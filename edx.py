a = int(input( "Ingrese el primer numero: "))
b = int(input( "Ingrese el segundo numero: "))
c = int(input( "Ingrese el tercer numero: "))
minimo = min(a, b, c)
maximo = max(a, b, c)
intermedio = (a + b + c) - minimo - maximo
print(minimo,intermedio,maximo)