asignaturas = ["matematicas", "fisica", "quimica", "lenguaje"]
notas = []
for asig in asignaturas:
    notas.append(float(input(f"ingrese su nota en la asignatura {asig}")))
    
print(asignaturas)
print(notas)

suma = 0
for nota in notas:
    suma += nota
print("El promedio es: ", suma/len(notas))

for indice in range(len(notas)):
    print(asignaturas[indice], "\t", notas[indice])