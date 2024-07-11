numeros = [98765432, 98767654, 965738273]
nombres = ["eduardo", "romina", "pamela"]
apellidos = ["jaramillo", "huentelao", "soto"]

persona = 2

print(f"{nombres[persona]} {apellidos[persona]} {numeros[persona]}")

ingresar_n = input("Ingrese un nombre")
ingresar_a = input("Iese apellido")
ingresar_t = int(input("Ingrese el telefono"))

nombres.append(ingresar_n)
apellidos.append(ingresar_a)
numeros.append(ingresar_t)

print(numeros)
print(nombres)
print(apellidos)