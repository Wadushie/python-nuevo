import random

# Declaraciones
rondas = 0
puntaje_J1 = []
puntaje_J2 = []
contador_victorias_J1 = 0
contador_victorias_J2 = 0

# Inicio del programa
def jugar(jugador, puntaje, contador_victorias, puntajes_jugador2):
    dado1 = random.randint(1, 7)
    dado2 = random.randint(1, 7)
    sumadados = dado1 + dado2
    print("Los valores de los dados para el Jugador", jugador, " son: ", dado1, " y ", dado2)
    print("La suma de ambos dados para el Jugador", jugador, " es: ", sumadados, "\n")
    if sumadados == 7:
        print("La suma de los dados generados aleatoriamente llegó a 7!!!!!")
        print("Gana el Jugador ", jugador, "!")
        puntaje.append(sumadados)
        print("El puntaje del Jugador 1 es: ", puntaje)
        contador_victorias = contador_victorias + 1
        print("Cantidad de victorias del Jugador 1: ", contador_victorias)
    else:
        if sumadados != 7:
            print("No fue el número ganador :(")
            puntaje.append(sumadados)
            print("El puntaje del Jugador 1 es: ", puntaje)
            print("\n")
    if dado1 == dado2:
        print("El Jugador 1 pierde la ronda :(")
        print("Gana el Jugador 2!")
        puntajes_jugador2.append(sumadados)
        print("Turno del siguiente jugador")

def empate(contador_victorias, sumatoria, jugador):
    if contador_victorias == contador_victorias:
        print("Es un empate! Determinando ganador de la ronda...")
        sumatoria_J1 = sum(puntaje_J1)
        sumatoria_J2 = sum(puntaje_J2)
        if sumatoria_J1 > sumatoria_J2:
            print("Gana el Jugador 1 con una suma total de puntos de", sumatoria_J1)
            contador_victorias += 1
        elif sumatoria_J2 > sumatoria_J1:
            print("Gana el Jugador 2 con una suma total de puntos de", sumatoria_J2)
            contador_victorias += 1
        else:
            print("Empate en la ronda. No hay ganador.")

while True:
    while rondas < 10:
        dado1_J1 = random.randint(1, 7)
        dado2_J1 = random.randint(1, 7)
        dado1_J2 = random.randint(1, 7)
        dado2_J2 = random.randint(1, 7)

        print("¿Quién juega primero? (1 = Jugador_1 / 2 = Jugador_2)")
        seleccion = int(input())
        # JUGADOR 1
        if seleccion == 1:
            jugar(puntaje_J1, contador_victorias_J1, puntaje_J2)

        # Caso de empate

        rondas = rondas + 1
        print("La ronda actual es: ", rondas)
        if rondas > 5:
            print("Quiere sumar o restar 1 al valor de un dado (s/n)")
            decision = input()
            if decision.lower() == 's':
                print("Cual de los dos dados quiere modificar (1 = dado1 / 2 = dado2): ")
                elegir = int(input())
                if elegir == 1:
                    dado1_J1 += 1
                elif elegir == 2:
                    dado2_J1 += 1
            else:
                sumadados = dado1_J1 + dado2_J1

        # JUGADOR 2
        if seleccion == 2:
            sumadados = dado1_J2 + dado2_J2
            print("Los valores de los dados para el Jugador 2 son: ", dado1_J2, " y ", dado2_J2)
            print("La suma de ambos dados para el Jugador 2 es: ", sumadados, "\n")
            if sumadados == 7:
                print("Gana el Jugador 2)))))!!!!!")
                puntaje_J2.append(sumadados)
                print("El puntaje del Jugador 2 es: ", puntaje_J2)
                contador_victorias_J2 = contador_victorias_J2 + 1
                print("Cantidad de victorias del Jugador 2: ", contador_victorias_J2)
            else:
                if sumadados != 7:
                    print("No fue el número ganador :(")
                    puntaje_J2.append(sumadados)
                    print("El puntaje del Jugador 2 es: ", puntaje_J2)
                    print("\n")
            if dado1_J2 == dado2_J2:
                print("El Jugador 2 pierde la ronda :(")
                print("Gana el Jugador 1!")
                puntaje_J1.append(sumadados)
                print("Turno del siguiente jugador")
        # Caso de empate
        empate()
        if contador_victorias_J2 == contador_victorias_J1:
            print("Es un empate! El ganador de la ronda...")
            sumatoria_J1 = sum(puntaje_J1)
            sumatoria_J2 = sum(puntaje_J2)
            if sumatoria_J1 > sumatoria_J2:
                print("Gana el Jugador 1 con una suma total de puntos de", sumatoria_J1)
                contador_victorias_J1 += 1
            elif sumatoria_J2 > sumatoria_J1:
                print("Gana el Jugador 2 con una suma total de puntos de", sumatoria_J2)
                contador_victorias_J2 += 1
            else:
                print("Empate en la ronda. No hay ganador.")

        print("La ronda actual es: ", rondas)
        if rondas > 5:
            print("Quiere sumar o restar 1 al valor de un dado (s/n)")
            decision = input()
            if decision.lower() == 's':
                print("Cual de los dos dados quiere modificar (1 = dado1 / 2 = dado2): ")
                elegir = int(input())
                if elegir == 1:
                    dado1_J2 += 1
                elif elegir == 2:
                    dado2_J2 += 1
            else:
                sumadados = dado1_J2 + dado2_J2
    # Ganador del juego!
    if rondas >= 10:
        print("El jugador con más victorias es: ")
        if contador_victorias_J1 > contador_victorias_J2:
            print("El Jugador 1 gano la partida!")
        elif contador_victorias_J2 > contador_victorias_J1:
            print("El Jugador 2 gano la partida!")

    reiniciar = input("¿Quieres iniciar el juego de nuevo? (S/N): ")
    if reiniciar.lower() != 's':
        break
