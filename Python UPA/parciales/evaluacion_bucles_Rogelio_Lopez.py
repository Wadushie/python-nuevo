# Escribir un programa que permita a dos personas jugar el juego de sumar 50. La suma se irá
# obteniendo a partir de números generados de manera aleatoria. Las reglas del nuevo se indican a
# continuación:
# 1. El programa debe permitir el juego entre dos jugadores.
# 2. Por cada jugador el programa deberá contar con una variable de puntuación que indicará
# el puntaje obtenido hasta el momento y una variable de penalización que indicará la
# penalización obtenida hasta el momento.
# 3. Para iniciar el juego, el programa deberá generar tres números aleatorios entre 10 y 30. El
# jugador deberá elegir uno de los números generados para inicializar la variable puntuación.
# 4. Una vez inicializada la variable de puntuación, el programa deberá generar números
# aleatorios entre 1 y 15.
# 5. El programa deberá permitir varias rondas del juego hasta que uno de los jugadores llegue
# al valor 50 en su variable de puntuación o que uno de los jugadores quede descalificado.
# 6. El programa deberá generar tres números aleatorios para cada jugador en cada ronda del
# juego.
# 7. El jugador deberá seleccionar los números que quiere utilizar.
# 8. El jugador deberá indicar si los números elegidos serán sumados o restados de su variable
# de puntuación.
# 9. Los números no utilizados serán sumados o restados de su variable de penalización
# dependiendo de la operación seleccionada en el punto 7.
# 10. Por cada ronda se deberán indicar los valores de las variables de puntuación y
# penalización de cada jugador.
# 11. El juego termina cuando uno de los jugadores llega al valor 50 en su variable de
# puntuación.
# 12. El jugador que supere el valor de 30 o -30 en su variable de penalización será
# descalificado del juego y el otro jugador quedará como ganador.
# 13. Una vez que el programa indique el ganador el juego, el programa deberá consultar si se
# quiere iniciar de vuelta el juego. De ser afirmativa la respuesta, el juego vuelve a iniciar.

import random

# Declaraciones
jugador1_puntaje = random.randint(1, 15)
jugador1_penalizacion = 0
jugador2_puntaje = random.randint(1, 15)
jugador2_penalizacion = 0

while True:
    print("---------------------------------------------------------------------------------")
    print("El puntaje inicial del jugador 1 es:", jugador1_puntaje)
    print("El puntaje inicial del jugador 2 es:", jugador2_puntaje)

    # Generacion de 3 numeros enteros para cada jugador
    num1_aleatorio_J1 = random.randint(1, 30)
    num2_aleatorio_J1 = random.randint(1, 30)
    num3_aleatorio_J1 = random.randint(1, 30)
    print(f"Los números generados para el jugador 1 son: {num1_aleatorio_J1}, {num2_aleatorio_J1}, {num3_aleatorio_J1}")

    num1_aleatorio_J2 = random.randint(1, 30)
    num2_aleatorio_J2 = random.randint(1, 30)
    num3_aleatorio_J2 = random.randint(1, 30)
    print(f"Los números generados para el jugador 2 son: {num1_aleatorio_J2}, {num2_aleatorio_J2}, {num3_aleatorio_J2}")

    while True:
        # TURNO JUGADOR 1
        operacionJ1 = int(input("\nPara el jugador 1, ¿Qué operación deseas realizar?\nIngresa 1 para suma o 2 para resta: "))
        while operacionJ1 < 1 or operacionJ1 > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2.")
            operacionJ1 = int(input("\nPara el jugador 1, ¿Qué operación deseas realizar?\nIngresa 1 para suma o 2 para resta: "))

        usar = int(input("\nJugador 1, ¿Deseas usar el primer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 1, ¿Deseas usar el primer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))

        if usar == 1:
            if operacionJ1 == 1:  # sumar
                jugador1_puntaje += num1_aleatorio_J1
            elif operacionJ1 == 2:  # restar
                jugador1_puntaje -= num1_aleatorio_J1
        elif usar == 2:  # no usar
            if operacionJ1 == 1:  # sumar
                jugador1_penalizacion += num1_aleatorio_J1
            elif operacionJ1 == 2:  # restar
                jugador1_penalizacion -= num1_aleatorio_J1

        usar = int(input("\nJugador 1, ¿Deseas usar el segundo número aleatorio?\nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 1, ¿Deseas usar el segundo número aleatorio?\nIngresa 1 para Sí o 2 para No: "))

        if usar == 1:
            if operacionJ1 == 1:  # sumar
                jugador1_puntaje += num2_aleatorio_J1
            elif operacionJ1 == 2:  # restar
                jugador1_puntaje -= num2_aleatorio_J1
        elif usar == 2:  # no usar
            if operacionJ1 == 1:  # sumar
                jugador1_penalizacion += num2_aleatorio_J1
            elif operacionJ1 == 2:  # restar
                jugador1_penalizacion -= num2_aleatorio_J1

        usar = int(input("\nJugador 1, ¿Deseas usar el tercer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 1, ¿Deseas usar el tercer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))

        if usar == 1:
            if operacionJ1 == 1:  # sumar
                jugador1_puntaje += num3_aleatorio_J1
            elif operacionJ1 == 2:  # restar
                jugador1_puntaje -= num3_aleatorio_J1
        elif usar == 2:  # no usar
            if operacionJ1 == 1:  # sumar
                jugador1_penalizacion += num3_aleatorio_J1
            elif operacionJ1 == 2:  # restar
                jugador1_penalizacion -= num3_aleatorio_J1

        # Mostrar puntaje y penalización del jugador 1
        print(f"Puntaje del jugador 1: {jugador1_puntaje}")
        print(f"Penalización del jugador 1: {jugador1_penalizacion}")
        if jugador1_puntaje >= 50:
            print("¡El jugador 1 ha ganado!")
            break

        if abs(jugador1_penalizacion) > 30 or abs(jugador1_penalizacion) < -30:
            print("¡El jugador 1 ha sido descalificado!")
            print("¡El jugador 2 ha ganado!")
            break

        # TURNO JUGADOR 2
        operacionJ2 = int(input("\nPara el jugador 2, ¿Qué operación deseas realizar?\nIngresa 1 para suma o 2 para resta: "))
        while operacionJ2 < 1 or operacionJ2 > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2.")
            operacionJ2 = int(input("\nPara el jugador 2, ¿Qué operación deseas realizar?\nIngresa 1 para suma o 2 para resta: "))

        usar = int(input("\nJugador 2, ¿Deseas usar el primer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 2, ¿Deseas usar el primer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))

        if usar == 1:
            if operacionJ2 == 1:  # sumar
                jugador2_puntaje += num1_aleatorio_J2
            elif operacionJ2 == 2:  # restar
                jugador2_puntaje -= num1_aleatorio_J2
        elif usar == 2:  # no usar
            if operacionJ2 == 1:  # sumar
                jugador2_penalizacion += num1_aleatorio_J2
            elif operacionJ2 == 2:  # restar
                jugador2_penalizacion -= num1_aleatorio_J2

        usar = int(input("\nJugador 2, ¿Deseas usar el segundo número aleatorio?\nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 2, ¿Deseas usar el segundo número aleatorio?\nIngresa 1 para Sí o 2 para No: "))

        if usar == 1:
            if operacionJ2 == 1:  # sumar
                jugador2_puntaje += num2_aleatorio_J2
            elif operacionJ2 == 2:  # restar
                jugador2_puntaje -= num2_aleatorio_J2
        elif usar == 2:  # no usar
            if operacionJ2 == 1:  # sumar
                jugador2_penalizacion += num2_aleatorio_J2
            elif operacionJ2 == 2:  # restar
                jugador2_penalizacion -= num2_aleatorio_J2

        usar = int(input("\nJugador 2, ¿Deseas usar el tercer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 2, ¿Deseas usar el tercer número aleatorio?\nIngresa 1 para Sí o 2 para No: "))

        if usar == 1:
            if operacionJ2 == 1:  # sumar
                jugador2_puntaje += num3_aleatorio_J2
            elif operacionJ2 == 2:  # restar
                jugador2_puntaje -= num3_aleatorio_J2
        elif usar == 2:  # no usar
            if operacionJ2 == 1:  # sumar
                jugador2_penalizacion += num3_aleatorio_J2
            elif operacionJ2 == 2:  # restar
                jugador2_penalizacion -= num3_aleatorio_J2

        # Mostrar puntaje y penalización del jugador 2
        print(f"Puntaje del jugador 2: {jugador2_puntaje}")
        print(f"Penalización del jugador 2: {jugador2_penalizacion}")
        if jugador2_puntaje >= 50:
            print("¡El jugador 2 ha ganado!")
            break

        if abs(jugador2_penalizacion) > 30 or abs(jugador2_penalizacion) < -30:
            print("¡El jugador 2 ha sido descalificado!")
            print("¡El jugador 1 ha ganado!")
            break

    reiniciar = input("¿Quieres iniciar el juego de nuevo? (S/N): ")
    if reiniciar.lower() != 's':
        break