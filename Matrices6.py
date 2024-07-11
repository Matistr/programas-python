agenda = [["carlos", "perez", 5697627162],
["Fernando", "Niembro", 556728172],
["Manuel", "Detezanos", 5696271829]]

seguir = True

while seguir :
  nombre = input("Ingrese el nombre")
  apellido = input("Ingrese el apellido")
  telefono = int(input("Ingrese el numero"))

  contacto = [nombre, apellido, telefono]
  agenda.append(contacto)

  seguir = bool(int(input("quiere seguir (0 para no; 1 para si)")))

print(agenda)