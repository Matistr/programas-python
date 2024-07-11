#Busca si hay aunque sea un numero dentro de una palabra
def buscar_num(palabra):
	x = any(chr.isdigit() for chr in palabra)
	return x

def conf_letra(palabra):
	x = palabra.isalpha()
	return x
a = "casa"
b = "1234567890"
print(conf_letra(a))