# Escribir un programa que permita a dos personas jugar el juego de sumar 50. La suma se irá
# obteniendo a partir de números generados de manera aleatoria. Las reglas del nuevo se indican a
# continuación:
# 1. El programa debe permitir el juego entre dos jugadores.
# 2. Por cada jugador el programa deberá contar con una variable de puntuación que indicará
# el puntaje obtenido hasta el momento.
# 3. Para iniciar el juego, el programa deberá generar de manera aleatoria, una lista con 20
# números del 5 y 10.
# 4. El programa deberá permitir varias rondas del juego hasta que uno de los jugadores llegue
# al valor 50 en su variable de puntuación.
# 5. En cada ronda el sistema deberá mostrar la lista de números generados de manera
# aleatoria y la puntuación del jugador. Cada jugador deberá indicar la posición en la lista del
# número que quiere utilizar.
# 6. El programa deberá sumar el número elegido a la puntuación del jugador y en la posición
# del número en la lista, se deberá cargar cero para que el número ya no sea utilizado.
# 7. El juego termina cuando uno de los jugadores llega al valor 50 en su variable de
# puntuación.
# 8. Una vez que el programa indique el ganador el juego, el programa deberá consultar si se
# quiere iniciar de vuelta el juego. De ser afirmativa la respuesta, el juego vuelve a iniciar.
# 9. En el caso que ya no queden números a elegir en lista y ninguno de los jugadores tiene
# puntaje para ganar, el sistema deberá generar un número aleatorio entre 1 y 15 y sumar al
# puntaje de cada jugador. Gana el jugador que más se acerque a 50.
import random
puntuacion_jugador1 = 0
puntuacion_jugador2 = 0
lista_jugadores = []
numero_aleat_nuevo = random.randint(1, 15)
puntaje_jugador1_nuevo = 0
puntaje_jugador2_nuevo = 0
condicion = True
    # Generacion de Numeros
for x in range(20):
    num = random.randint(5, 10)
    lista_jugadores.append(num)
print("Los valores de los vectores son: ")
print(lista_jugadores)

while True:
    # Selector de numero  generado que cuenta hasta 50
    print("Las posiciones del vector van del 0 al 19 en el teclado")
        # JUGADOR 1
    print("Jugador 1, Cual es la posicion dentro del vector que quiere usar?")
    posicion = int(input())
    puntuacion_jugador1 = puntuacion_jugador1 + lista_jugadores[posicion]
    print("El numero elegido fue ", lista_jugadores[posicion])
    lista_jugadores[posicion] = 0
    print(lista_jugadores)
    print("La puntuacion actual del jugador 1 es: ",puntuacion_jugador1)

        # JUGADOR 2
    print("Jugador 2, Cual es la posicion dentro del vector que quiere usar?")
    posicion = int(input())
    puntuacion_jugador2 = puntuacion_jugador2 + lista_jugadores[posicion]
    print("El numero elegido fue ", lista_jugadores[posicion])
    lista_jugadores[posicion] = 0
    print(lista_jugadores)
    print("La puntuacion del jugador 2 es: ",puntuacion_jugador2)


    if puntuacion_jugador1 > 50 or puntuacion_jugador2 > 50:
        suma_lista = sum(lista_jugadores)
        if suma_lista == 0:
            print("Ya no queda numeros a elegir")
            puntaje_jugador1_nuevo = numero_aleat_nuevo + puntuacion_jugador1
            puntaje_jugador2_nuevo = numero_aleat_nuevo + puntuacion_jugador2

            if abs(puntaje_jugador1_nuevo - 50) < abs(50 - puntaje_jugador2_nuevo):
                print("El jugador 1 es el ganador!")
                break
            elif abs(puntaje_jugador2_nuevo - 50) < abs(50 - puntaje_jugador1_nuevo):
                print("El jugador 2 es el ganador!")
                break
            else:
                print("Es un empate!")
                break
        else:
            if puntuacion_jugador1 > 50:
                print("El jugador 1 es el ganador!")
            elif puntuacion_jugador2 > 50:
                print("El jugador 2 es el ganador!")

        # Seguir jugando o no
        condicion = (input("Queres volver a jugar?")).lower()
        if condicion == "si":
            break
        elif condicion == "no":
            break