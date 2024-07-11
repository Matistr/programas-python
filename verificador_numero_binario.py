num = input("Ingrese una serie numerica: ")
largo = len(num)
cont = 0
es_binario = True
while cont < largo:
    if not(("0" in num[cont]) or ("1" in num[cont])):
        es_binario = False
    cont = cont + 1    
if es_binario:
    print("Es un binario")
else:
    print("No es binario")
