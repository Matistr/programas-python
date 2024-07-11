#Fase configuración 1.1.1
players = [[0 for _ in range(2)] for _ in range(2)]
print("Bienvenido al juego adivina-palabra")
players[0][0] = input("Ingrese el nombre del primer jugador: ")
players[1][0] = input("Ingrese el nombre del segundo jugador: ")
nro_palabras = int(input("Ingrese cantidad de palabras que deben adivinar: "))
max_intentos = int(input("Ingrese cantidad máxima de intentos para adivinar cada palabra: "))
rondas = nro_palabras
#Fase de proposicion-adivinacion 1.1.2
#Rondas impares adivinador para j1, rondas pares proponedor para j1.
def par_impar(num):
    resto = num % 2
    valor = False
    if resto == 0:
        valor = True
    return valor
def alternar(player):
    if player == players[0][0]:
        newplayer = players[1][0]
    else:
        newplayer = players[0][0]
    return newplayer
#Posición(es) de la letra dentro de la palabra
def posicion(palabra, letra):
    cadena = ""
    if palabra.count(letra) >0:
       for x in range(0, len(palabra)):
            if letra == palabra[x]:
                cadena = cadena + str(x + 1) + ","
    return cadena[0:len(cadena) - 1]
#Funcion ganador.
#Coomparar puntajes de los jugadores. El puntaje mayor, nombrarlo ganador.
def Ganador(puntaje):
    if puntaje[0] > puntaje[1]:
        Ganador = 0 #Gana el primer jugador
    elif puntaje[0] < puntaje[1]:
        Ganador = 1 #Gana el segundo jugador
    else:
        Ganador = 2 #Esto es un empate
    return Ganador
#Función que confirma que la palabra sólo contenga letras
def conf_letra(palabra):
	x = palabra.isalpha()
	return x
#Iniciar rondas
puntaje_j1 = 0
puntaje_j2 = 0
indice_player = 0
i = 1
RompeJuego = False
while i < (rondas + 1) and RompeJuego == False:
    if i == 1:
        jugador_act = players[1][0]
        jugador_sec = players[0][0]
        indice_player = 0
    else:
        jugador_act = alternar(jugador_act)
        jugador_sec = alternar(jugador_sec)
        if indice_player == 0:
            indice_player = 1
        else:
            indice_player = 0
    print(f"Ahora juega Proponedor: {jugador_act} - proponedor.")
    word = input("Ingrese palabra a adivinar: ")
    count = 1
    while (len(word) > 20 or not word.islower() or conf_letra(word) == False) and count <= 3:
        if len(word) > 20:
            print("La palabra no puede tener más de 20 carácteres.")
        if conf_letra(word) == False:
            print("La palabra sólo debe contener letras.")
        if not word.islower():
            print("La palabra debe estar en minúsculas.")
        word = input(f"{jugador_act} Por favor, ingrese palabra a adivinar: ")
        count = count + 1
    if count == 4:
        print(f"Gana Adivinador {jugador_sec}. El Proponedor excedió el máximo de intentos para ingresar una palabra.")
        RompeJuego = True
    else:
        letras_adiv = 0
        intentos = 1
        while intentos <= max_intentos and letras_adiv < len(word):
            print(f"Ahora juega Adivinador. {jugador_sec} - adivinador.")
            que_letra = input("¿Qué letra cree que tenga la palabra propuesta? : ")
            que_letra = que_letra[0]
            sistema = posicion(word, que_letra)
            if sistema != "":
                print(f"¡La letra pertenece a la palabra! Se encuentra en la posición: {sistema}")
                sistema = sistema.split(",")
                letras_adiv = letras_adiv + len(sistema)
            else:
                print("La letra no pertenece a la palabra, vuelva a intentar.")
                intentos = intentos + 1
        if intentos > max_intentos:
            print(f"Adivinador ha completado los intentos, la palabra a adivinar era: {word}")
            intentos = intentos - 1
        if letras_adiv == len(word):
            print("¡Adivinó todas las letras de la palabra!")
            #Calcular puntaje y pasar a la siguiente ronda
    i += 1
    if not RompeJuego:
        puntaje = (1 - (intentos / max_intentos)) * len(word)
        players[indice_player][1] = players[indice_player][1] + puntaje
if not RompeJuego:
    lista = players[0][1], players[1][1]
    resultado_puntajes = Ganador(lista)
    if resultado_puntajes == 2:
        print("No hay ganadores, es un empate. El puntaje es: " + str(players[0][1]))
    elif resultado_puntajes == 1:
        print("El ganador y su puntaje son: " + str(players[1][0]) + " " + str(players[1][1]))
        print("El perdedor y su puntaje son: " + str(players[0][0]) + " " + str(players[0][1]))
    else:
        print("El ganador y su puntaje son: " + str(players[0][0]) + " " + str(players[0][1]))
        print("El perdedor y su puntaje son: " + str(players[1][0]) + " " + str(players[1][1]))