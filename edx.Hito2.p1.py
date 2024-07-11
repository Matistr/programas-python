#Ejercicio 1
def suma_divisores(a):
    suma = 0
    #primo = True
    for divisor in range(1, a - 1):
        if (a % divisor) == 0:
            suma += divisor
            #primo = False
    if suma == 1:
        primo = True
    else:
        primo = False
    return suma, primo
#Ejercicio 2
import math
def area_triangulo(base,altura):
    area = (base * altura) / 2
    return area
def area_rectangulo(base,altura):
    area = base * altura
    return area
def area_rombo(diagonal1,diagonal2):
    area = (diagonal1 * diagonal2) / 2
    return area
def area_circulo(radio):
    area = math.pi * (radio**2)
    return area
#Ejercicio 3
def numero_perfecto(a):
    suma = 0
    for divisor in range(1, a - 1):
        if (a % divisor) == 0:
            suma += divisor
    if suma != a:
        return False
    elif suma == a:
        return True
#Ejercicio 4
def ocultar_letras(palabra,cantidad):
    for x in range(len(palabra)):
        pass   #####
    return palabra 

def revisar_letra(palabra_secreta,palabra,letra):
    return palabra
#Ejercicio 5
def jerigonzo(string):
    translado = ""
    for letra in string:
        if letra in "AEIOUaeiou":
            translado += letra
            translado += "p"
        translado += letra
    return translado
#Ejercicio 6
def buscarTodas(a,b):
	posiciones = ""
	posicion = 0
	while posicion != -1:
		posicion = a.find(b,posicion)
		if posicion != -1:
			posiciones = posiciones + " " + str(posicion)
			posicion += 1
	return posiciones.lstrip() #lstrip borra el espacio en blanco al priincipio de un string