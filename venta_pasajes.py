origen = []
with open("Ciudades_origen.txt", "r") as archivo:
    lineatxt = archivo.readlines()
    for i in lineatxt:
        origen.append(i)

destino = []
with open("Ciudades_destino.txt", "r") as archivo:
    lineatxt = archivo.readlines()
    for i in lineatxt:
        destino.append(i)

venta_pasajes = []

salir = 0
while salir != 1:
    print("Opcion 1: Venta de pasajes.")
    print("Opcion 2: Reporte de pasajes vendidos.")
    print("Ingresa 3 para salir")
    opcion = int(input("Ingrese su opcion: "))
    if opcion == 1:
        print(origen)
        ciudad_origen = input("Por favor indique ciudad de origen: ")
        ciudad_destino = ciudad_origen
        while ciudad_destino == ciudad_origen:
           print(destino)
           ciudad_destino = input("Por favor indique ciudad de destino: ")
        fecha_viaje = input("Ingrese la fecha en la que desea viajar: ")
        hora_salida = input("Ingrese la hora de salida: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        fecha_nacimiento = input("Ingrese fecha de su nacimiento: ")
        registro = [nombre, apellido, fecha_nacimiento, ciudad_origen, ciudad_destino, fecha_viaje, hora_salida]
        venta_pasajes.append(registro)
        print("Su pasaje ha sido registrado.")

    elif opcion == 2:
        print(venta_pasajes)

    elif opcion == 3:
        salir = 1
