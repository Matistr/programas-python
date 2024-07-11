#Busca s hay aunque sea un numero dentro de una palabra
def buscar_num(palabra):
	x = any(chr.isdigit() for chr in palabra)
	return x