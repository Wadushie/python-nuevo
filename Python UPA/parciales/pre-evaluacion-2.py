# Escribir un programa que permita a dos personas jugar el juego de sumar 15. La suma será
# obtenida de manera aleatoria para cada jugador. A continuación, las reglas del juego:
# 1. Cada jugador cuenta con dos variables: puntaje y penalización.
# 2. La variable puntaje deberá ser inicializada de manera aleatoria con un valor entre 1 y 20.
# 3. El programa deberá generar tres números aleatorios para cada jugador.
# 4. Los números generados estarán en el rango de 1 a 10.
# 5. El jugador deberá indicar los números a utilizar. (puede utilizar 1, 2 o los tres números
# generados). Al seleccionar los números se debe asegurar que los jugadores ingresen un
# valor correcto. Si el valor es incorrecto, el programa debe volver a pedir el valor.
# 6. El jugador deberá indicar la operación a realizar: sumar o restar. También se debe validar
# la entrada.
# 7. El programa deberá tomar los números indicados por cada jugador y realizar la operación
# sobre la variable puntaje. Es decir, tomar los números indicados y sumar o restar del
# puntaje.
# 8. Los números no seleccionados se deberán sumar a la variable penalización.
# 9. El jugador ganador será el que tenga la suma más cercana a 15 y que tenga la menor
# penalización.
# 10. El programa deberá consultar si quiere volver a jugar. De ser así, se debe reiniciar el juego.

import random
    # Declaraciones
jugador1_puntaje = random.randint(1,20)
jugador1_penalizacion = 0
jugador2_puntaje = random.randint(1,20)
jugador2_penalizacion = 0
condicion = True
    # Puntaje de los jugadores
while True:

    print("El puntaje inicial del jugador 1 es: ", jugador1_puntaje)
    print("El puntaje inicial del jugador 2 es: ", jugador2_puntaje)
    print("---------------------------------------------------------------------------------")
        # Generacion de 3 numeros enteros
    num1_aleatorio_J1 = random.randint(1,10)
    num2_aleatorio_J1 = random.randint(1,10)
    num3_aleatorio_J1 = random.randint(1,10)
    print(f"Los números generados para el jugador 1 son: {num1_aleatorio_J1}, {num2_aleatorio_J1}, {num3_aleatorio_J1} ")
    num1_aleatorio_J2 = random.randint(1,10)
    num2_aleatorio_J2 = random.randint(1,10)
    num3_aleatorio_J2 = random.randint(1,10)
    print(f"Los números generados para el jugador 2 son: {num1_aleatorio_J2}, {num2_aleatorio_J2}, {num3_aleatorio_J2}")
    print("---------------------------------------------------------------------------------")

    # TURNO JUGADOR 1
    condicion = "si"
    operacionJ1 = int(input("\nPara el jugador 1, ¿Qué operación deseas realizar? \nIngresa 1 para suma o 2 para resta: "))
    while operacionJ1 < 1 or operacionJ1 > 2:
        print("Opcion incorrecta, las disponibles son 1 y 2.")
    operacionJ1 = int(input("\nPara el jugador 1, ¿Qué operación deseas realizar? \nIngresa 1 para suma o 2 para resta: "))
    print("----------------------------------------------------------------------------------")
    usar = int(input("\nJugador 1, ¿Deseas usar el primer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
    while usar < 1 or usar > 2:
        print("Opcion incorrecta, las disponibles son 1 y 2")
        usar = int(input("\nJugador 1, ¿Deseas usar el primer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
    if usar == 1:
        if operacionJ1 == 1: #sumar
            jugador1_puntaje = jugador1_puntaje + num1_aleatorio_J1
        elif operacionJ1 == 2: #restar
            jugador1_puntaje = jugador1_puntaje - num1_aleatorio_J1
        elif usar == 2: #no usar
            if operacionJ1 == 1: #sumar
                jugador1_penalizacion = jugador1_penalizacion + num1_aleatorio_J1
            elif operacionJ1 == 2: #restar
                jugador1_penalizacion = jugador1_penalizacion - num1_aleatorio_J1

    usar = int(input("\nJugador 1, ¿Deseas usar el segundo número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
    while usar < 1 or usar > 2:
        print("Opcion incorrecta, las disponibles son 1 y 2")
        usar = int(input("\nJugador 1, ¿Deseas usar el segundo número aleatorio? \nIngresa 1 para Sí o 2 para No: "))

    if usar == 1:
        if operacionJ1 == 1: #sumar
            jugador1_puntaje = jugador1_puntaje + num2_aleatorio_J1
        elif operacionJ1 == 2: #restar
            jugador1_puntaje = jugador1_puntaje - num2_aleatorio_J1
        elif usar == 2: #no usar
            if operacionJ1 == 1: #sumar
                jugador1_penalizacion = jugador1_penalizacion + num2_aleatorio_J1
            elif operacionJ1 == 2: #restar
                jugador1_penalizacion = jugador1_penalizacion - num2_aleatorio_J1

    usar = int(input("\nJugador 1, ¿Deseas usar el tercer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
    while usar < 1 or usar > 2:
        print("Opcion incorrecta, las disponibles son 1 y 2")
        usar = int(input("\nJugador 1, ¿Deseas usar el tercer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))

    if usar == 1:
        if operacionJ1 == 1: #sumar
            jugador1_puntaje = jugador1_puntaje + num3_aleatorio_J1
        elif operacionJ1 == 2: #restar
            jugador1_puntaje = jugador1_puntaje - num3_aleatorio_J1
        elif usar == 2: #no usar
            if operacionJ1 == 1: #sumar
                jugador1_penalizacion = jugador1_penalizacion + num3_aleatorio_J1
            elif operacionJ1 == 2: #restar
                jugador1_penalizacion = jugador1_penalizacion - num3_aleatorio_J1


        # TURNO JUGADOR 2
        operacionJ2 = int(input("\nPara el jugador 2, ¿Qué operación deseas realizar? \nIngresa 1 para suma o 2 para resta: "))
        while operacionJ2 < 1 or operacionJ2 > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2.")
            operacionJ2 = int(input("\nPara el jugador 2, ¿Qué operación deseas realizar? \nIngresa 1 para suma o 2 para resta: "))
        print("----------------------------------------------------------------------------------")
        usar = int(input("\nJugador 2, ¿Deseas usar el primer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 2, ¿Deseas usar el primer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
        if usar == 1: #usar
            if operacionJ2 == 1: #sumar
                jugador2_puntaje = jugador2_puntaje + num1_aleatorio_J2
            elif operacionJ2 == 2: #restar
                jugador2_puntaje = jugador2_puntaje - num1_aleatorio_J2
        elif usar == 2: #no usar
            if operacionJ2 == 1: #sumar
                jugador2_penalizacion = jugador2_penalizacion + num1_aleatorio_J2
            elif operacionJ2 == 2: #restar
                jugador2_penalizacion = jugador2_penalizacion - num1_aleatorio_J2

        usar = int(input("\nJugador 2, ¿Deseas usar el segundo número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 2, ¿Deseas usar el segundo número aleatorio? \nIngresa 1 para Sí o 2 para No: "))

        if usar == 1: #usar
            if operacionJ2 == 1: #sumar
                jugador2_puntaje = jugador2_puntaje + num2_aleatorio_J2
            elif operacionJ2 == 2: #restar
                jugador2_puntaje = jugador2_puntaje - num2_aleatorio_J2
        elif usar == 2: #no usar
            if operacionJ2 == 1: #sumar
                jugador2_penalizacion = jugador2_penalizacion + num2_aleatorio_J2
            elif operacionJ2 == 2: #restar
                jugador2_penalizacion = jugador2_penalizacion - num2_aleatorio_J2

        usar = int(input("\nJugador 2, ¿Deseas usar el tercer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
        while usar < 1 or usar > 2:
            print("Opcion incorrecta, las disponibles son 1 y 2")
            usar = int(input("\nJugador 2, ¿Deseas usar el tercer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))

        if usar == 1: #usar
            if operacionJ2 == 1: #sumar
                jugador2_puntaje = jugador2_puntaje + num3_aleatorio_J2
            elif operacionJ2 == 2: #restar
                jugador2_puntaje = jugador2_puntaje - num3_aleatorio_J2
        elif usar == 2: #no usar
            if operacionJ2 == 1: #sumar
                jugador2_penalizacion = jugador2_penalizacion + num3_aleatorio_J2
            elif operacionJ2 == 2: #restar
                jugador2_penalizacion = jugador2_penalizacion - num3_aleatorio_J2

        ### DIFERENCIA ENTRE LAS SUMAS SIENDO LA MAS CERCANA A 15 ###
        diferencia = 15
        resultado = input("Ahora para calcular los resultados, se deberá diferenciar las sumas y restas siendo más cercana a 15")
        ganador = int
        if abs(jugador1_puntaje - diferencia) < abs(jugador2_puntaje - diferencia):
            ganador = 1
        elif abs(jugador1_puntaje - diferencia) > abs(jugador2_puntaje - diferencia):
            ganador = 2
        else:
            if jugador1_penalizacion < jugador2_penalizacion:
                ganador = 1
            elif jugador1_penalizacion > jugador2_penalizacion:
                ganador = 2
            else:
                ganador = 0
        if ganador == 0:
            print("\n¡Es un empate!")
        else:
            print(f"\n¡El Jugador {ganador} ha ganado!")

        # Declaracion de Turnos
        condicion = (input("Queres seguir jugando?, Pone si o no")).lower()
        if condicion != "si":
            break
        # Revisar porque realiza un bucle en los turnos enves de pedir si seguir jugando :(