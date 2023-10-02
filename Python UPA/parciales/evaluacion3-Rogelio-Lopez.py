# Escribir un programa que permita a dos personas jugar el juego "sumar 50". Las reglas se
# describen a continuación:
# 1. El juego debe permitir el enfrentamiento entre dos jugadores: jugador A y jugador B.
# 2. Ambos jugadores inician con un puntaje de 0.
# 3. Al inicio del juego, se generará una lista de 20 números aleatorios entre 1 y 10. Estos
# números son los que los jugadores pueden elegir para ir sumando a su puntaje.
# 4. Los jugadores podrán elegir los números seleccionados de la lista de manera alternada. En
# cada turno, el sistema mostrará la lista de números y el puntaje de ambos jugadores.
# Luego, el jugador en turno deberá elegir un número de la lista proporcionando su posición.
# 5. Una vez que un jugador elige un número de la lista, ese número se convierte en 0,
# indicando que ya no puede ser elegido.
# 6. El juego avanza en rondas, alternando entre los jugadores.
# 7. Si un jugador selecciona un número que resulta en un puntaje mayor a 50, ese jugador
# pierde automáticamente y el otro jugador es declarado ganador.
# 8. Si un jugador llega exactamente a 50, ese jugador es declarado ganador.
# 9. Si la lista se agota y ninguno de los jugadores ha llegado a 50, entonces se generará un
# número "bonus" para cada jugador entre 1 y 15 que se suma al puntaje de cada jugador. El
# ganador será el jugador cuyo puntaje esté más cerca de 50.
# 10. Una vez que se declare un ganador, el programa deberá preguntar si se quiere jugar otra
# partida. Si la respuesta es afirmativa, el juego reinicia.
# 11. Los jugadores pueden elegir "saltar" su turno hasta 3 veces en total. Al saltar, no
# seleccionan un número de la lista, pero el número más alto de la lista se convierte en 0 (si
# el número más alto aparece varias veces, solo uno se convierte en cero). Si ambos
# jugadores eligen saltar en la misma ronda, el número más bajo de la lista se suma al
# puntaje de ambos.

# 12. Cada jugador tiene un "comodín". Una vez por juego, un jugador puede usar su comodín
# para duplicar el número que elige ese turno.
# 13. Si un jugador elige un número que es adyacente (anterior o siguiente) a un 0 en la lista,
# ese jugador recibe un bonus de +2 en su puntaje. Por ejemplo, si la lista es [7,0,9,6,...] y el
# jugador elige el 9, recibe 11 puntos en total.
import random

while True:
    # Declaraciones
    puntuacion_jugadorA = 0
    puntuacion_jugadorB = 0
    numero_aleatorio_bonus = random.randint(1, 15)
    puntaje_jugadorA_nuevo = 0
    puntaje_jugadorB_nuevo = 0
    lista_jugadores = []
    mayor_numero = 0
    Salto_jugadorA = 3
    Salto_jugadorB = 3
    condicion = True
    comodin_jugadorA_usado = False
    comodin_jugadorB_usado = False

    # Creación de tabla de 20 segmentos con números aleatorios de 1 al 10
    for x in range(20):
        num = random.randint(1, 10)
        lista_jugadores.append(num)
    print("Los valores de los vectores son: ")
    print(lista_jugadores)

    # Inicio del ciclo de turnos
    while True:
        # Selector de número generado que cuenta hasta 50
        # JUGADOR A
        if Salto_jugadorA > 0:
            opcion = input("Jugador A, Elija si quiere jugar su turno o saltar, (1 = Jugar / 2 = Saltar)")
            if opcion == "1":
                if not comodin_jugadorA_usado:
                    usar_comodin = input("¿Desea usar su comodín para duplicar el número? (si/no): ")
                    if usar_comodin.lower() == 'si':
                        posicion = int(input("Jugador A, ¿Cuál es la posición dentro del vector que quiere usar?"))
                        lista_jugadores[posicion] *= 2
                        comodin_jugadorA_usado = True
                    else:
                        print("Jugador A, ¿Cuál es la posición dentro del vector que quiere usar?")
                        posicion = int(input())
                else:
                    print("Jugador A, ¿Cuál es la posición dentro del vector que quiere usar?")
                    posicion = int(input())
                numero_elegido = lista_jugadores[posicion]
                if posicion > 0 and lista_jugadores[posicion - 1] == 0:
                    puntuacion_jugadorA += 2  # Bonus +2
                elif posicion < len(lista_jugadores) - 1 and lista_jugadores[posicion + 1] == 0:
                    puntuacion_jugadorA += 2  # Bonus +2
                puntuacion_jugadorA += numero_elegido
                print("El número elegido fue ", numero_elegido)
                lista_jugadores[posicion] = 0
                print(lista_jugadores, "\n")
                print("La puntuación actual del jugador A es: ", puntuacion_jugadorA)
            elif opcion == '2':
                mayor_numero = max(lista_jugadores)
                lista_jugadores[lista_jugadores.index(mayor_numero)] = 0
                print("Jugador A ha elegido Saltar. El número más alto se convierte en 0.")
                Salto_jugadorA -= 1
                print(lista_jugadores)
            else:
                print("Opcion no identificada, elija devuelta")

        # JUGADOR B
        if Salto_jugadorB > 0:
            opcion = input("Jugador B, Elija si quiere jugar su turno o saltarlo, (1 = Jugar / 2 = Saltar)")
            if opcion == "1":
                if not comodin_jugadorB_usado:
                    usar_comodin = input("¿Desea usar su comodín para duplicar el número? (si/no): ")
                    if usar_comodin.lower() == 'si':
                        posicion = int(input("Jugador B, ¿Cuál es la posición dentro del vector que quiere usar?"))
                        lista_jugadores[posicion] *= 2
                        comodin_jugadorB_usado = True
                    else:
                        print("Jugador B, ¿Cuál es la posición dentro del vector que quiere usar?")
                        posicion = int(input())
                else:
                    print("Jugador B, ¿Cuál es la posición dentro del vector que quiere usar?")
                    posicion = int(input())
                numero_elegido = lista_jugadores[posicion]
                if posicion > 0 and lista_jugadores[posicion - 1] == 0:
                    puntuacion_jugadorB += 2  # Bonus +2
                elif posicion < len(lista_jugadores) - 1 and lista_jugadores[posicion + 1] == 0:
                    puntuacion_jugadorB += 2  # Bonus +2
                puntuacion_jugadorB += numero_elegido
                print("El número elegido fue ", numero_elegido)
                lista_jugadores[posicion] = 0
                print(lista_jugadores, "\n")
                print("La puntuación actual del jugador B es: ", puntuacion_jugadorB)
            elif opcion == '2':
                mayor_numero = max(lista_jugadores)
                lista_jugadores[lista_jugadores.index(mayor_numero)] = 0
                print("Jugador B ha elegido Saltar. El número más alto se convierte en 0.")
                Salto_jugadorB -= 1
                print(lista_jugadores)
            else:
                print("Opción no válida, intente nuevamente.")

        # Verificador de puntajes
        if puntuacion_jugadorA > 50:
            print("El jugador A pierde, ¡Gana el jugador B!")
            break
        elif puntuacion_jugadorB > 50:
            print("El jugador B pierde, ¡Gana el jugador A!")
            break
        elif puntuacion_jugadorA == 50:
            print("El jugador A es el ganador!")
            break
        else:
            if puntuacion_jugadorB == 50:
                print("El jugador B es el ganador!")
                break

        # Si la lista se agota
        suma_lista = sum(lista_jugadores)
        if suma_lista == 0:
            print("Ya no quedan números a elegir")
            puntaje_jugadorA_nuevo = numero_aleatorio_bonus + puntuacion_jugadorA
            puntaje_jugadorB_nuevo = numero_aleatorio_bonus + puntuacion_jugadorB

        if abs(puntaje_jugadorA_nuevo - 50) < abs(50 - puntaje_jugadorB_nuevo):
            print("El jugador A es el ganador!")
            break
        elif abs(puntaje_jugadorB_nuevo - 50) < abs(50 - puntaje_jugadorA_nuevo):
            print("El jugador B es el ganador!")
            break

    # Reinicio del juego al terminar
    reiniciar = input("¿Desea reiniciar el juego? (si/no): ")
    if reiniciar.lower() != 'si':
        break