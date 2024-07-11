matriz = [[17, 3, 50, 4, 85, 5, 26, 85, 19, 40],
 [66, 45, 55, 65, 8, 97, 39, 33, 89, 62],
 [74, 28, 44, 64, 10, 83, 2, 87, 74, 42],
 [72, 29, 20, 61, 63, 87, 86, 17, 68, 79],
 [79, 8, 18, 68, 31, 88, 21, 64, 96, 64],
 [88, 99, 50, 41, 16, 90, 71, 72, 68, 78],
 [76, 57, 5, 47, 8, 47, 97, 86, 52, 5],
 [77, 78, 9, 40, 29, 79, 25, 44, 66, 88],
 [98, 48, 75, 63, 6, 3, 57, 10, 37, 54],
 [43, 18, 62, 86, 96, 83, 30, 88, 3, 94]]
familia = ["soto", "perez", "abarza", "loyola", "cappuleto", "barbagelata", "valverde", "freire", "lavin", "rozales"]
aviones = ["LAN718", "LAN827", "SKY281", "IBERIA18", "LAN115", "LAN818", "LATAM811", "AIRCANADA181", "EMIRATES171", "SKY17"]
def info(m, f, a, x, y):
    return f"El pasajero tiene la edad de {m[x][y]} años, es de la familia {f[x]} y viaja en el avión {a[y]}."
x = int(input("Ingrese un numero para la fila: "))
y = int(input("Ingrese un numero para la columna: "))
print(info(matriz, familia, aviones, x, y))