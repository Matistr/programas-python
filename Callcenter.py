def llamada(nombre, agenda_diccionario):
    print("Llamando a ", nombre)
agenda = {}
nombre = input("Ingrese nombre del contacto: ")
numero = int(input("Ingrese numero del contacto: "))
direccion = input("Ingrese direccion del contacto: ")
agenda[nombre] = (numero, direccion)
for nombre,(numero,direccion) in agenda.items():
    print(nombre, numero, direccion)
llamada("Matias", agenda)