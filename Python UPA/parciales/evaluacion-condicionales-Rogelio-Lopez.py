"""
Escribir un programa que permita a dos personas jugar el juego de sumar 15.
La suma será obtenida de manera aleatoria para cada jugador.
A continuación, las reglas del juego:

1.	Cada jugador cuenta con dos variables: puntaje y penalización.
2.	La variable puntaje deberá ser inicializada de manera aleatoria con un valor entre 1 y 20.
3.	El programa deberá generar tres números aleatorios para cada jugador.
4.	Los números generados estarán en el rango de 1 a 10.
5.	El jugador deberá indicar los números a utilizar. (puede utilizar 1, 2 o los tres números generados)
6.	El jugador deberá indicar la operación a realizar: sumar o restar.
7.	El programa deberá tomar los números indicados por cada jugador y realizar la operación sobre la variable puntaje. Es decir, tomar los números indicados y sumar o restar del puntaje.
8.	Los números no seleccionados se deberán sumar a la variable penalización.
9.	El jugador ganador será el que tenga la suma más cercana a 15 y que tenga la menor penalización.
"""

import random
#Reglas para el Jugador1
puntaje_jug1 = random.randint(1,20)
puntaje_jug2 = random.randint(1,20)
penalizacionJ1 = 0
penalizacionJ2 = 0
num_aleatorio_J1_1 = random.randint(1,10)
num_aleatorio_J1_2 = random.randint(1,10)
num_aleatorio_J1_3 = random.randint(1,10)
num_aleatorio_J2_1 = random.randint(1,10)
num_aleatorio_J2_2 = random.randint(1,10)
num_aleatorio_J2_3 = random.randint(1,10)
print("Puntaje inicial del jugador 1: ", puntaje_jug1)
print("Puntaje inicial del jugador 2: ", puntaje_jug2)
print("Los números generados para el jugador 1 son: ", num_aleatorio_J1_1,"-", num_aleatorio_J1_2,"-", num_aleatorio_J1_3)
print("Los números generados para el jugador 2 son: ", num_aleatorio_J2_1,"-", num_aleatorio_J2_2,"-", num_aleatorio_J2_3)

operacionJ1 = int(input("\nPara el jugador 1, ¿Qué operación deseas realizar? \nIngresa 1 para suma o 2 para resta: "))
### INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO
usar = int(input("\nJugador 1, ¿Deseas usar el primer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
#ATENCIÓN: si el usuario no ingresa 1 0 2 el programa no funcionará
if usar == 1: #usar
    if operacionJ1 == 1: #sumar
        puntaje_jug1 = puntaje_jug1 + num_aleatorio_J1_1
    elif operacionJ1 == 2: #restar
        puntaje_jug1 = puntaje_jug1 - num_aleatorio_J1_1
elif usar == 2: #no usar
    if operacionJ1 == 1: #sumar
        penalizacionJ1 = penalizacionJ1 + num_aleatorio_J1_1
    elif operacionJ1 == 2: #restar
        penalizacionJ1 = penalizacionJ1 - num_aleatorio_J1_1
### FIN INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO

### INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO
usar = int(input("\nJugador 1, ¿Deseas usar el segundo número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
#ATENCIÓN: si el usuario no ingresa 1 0 2 el programa no funcionará
if usar == 1: #usar
    if operacionJ1 == 1: #sumar
        puntaje_jug1 = puntaje_jug1 + num_aleatorio_J1_2
    elif operacionJ1 == 2: #restar
        puntaje_jug1 = puntaje_jug1 - num_aleatorio_J1_2
elif usar == 2: #no usar
    if operacionJ1 == 1: #sumar
        penalizacionJ1 = penalizacionJ1 + num_aleatorio_J1_2
    elif operacionJ1 == 2: #restar
        penalizacionJ1 = penalizacionJ1 - num_aleatorio_J1_2
### FIN INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO

### INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO
usar = int(input("\nJugador 1, ¿Deseas usar el tercer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
#ATENCIÓN: si el usuario no ingresa 1 0 2 el programa no funcionará
if usar == 1: #usar
    if operacionJ1 == 1: #sumar
        puntaje_jug1 = puntaje_jug1 + num_aleatorio_J1_3
    elif operacionJ1 == 2: #restar
        puntaje_jug1 = puntaje_jug1 - num_aleatorio_J1_3
elif usar == 2: #no usar
    if operacionJ1 == 1: #sumar
        penalizacionJ1 = penalizacionJ1 + num_aleatorio_J1_3
    elif operacionJ1 == 2: #restar
        penalizacionJ1 = penalizacionJ1 - num_aleatorio_J1_3
### FIN INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO

###################################################################################################

operacionJ2 = int(input("\n¿Para el jugador 2, ¿Qué operación deseas realizar? \nIngresa 1 para suma o 2 para resta: "))
### INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO
usar = int(input("\nJugador 2, ¿Deseas usar el primer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
#ATENCIÓN: si el usuario no ingresa 1 0 2 el programa no funcionará
if usar == 1: #usar
    if operacionJ2 == 1: #sumar
        puntaje_jug2 = puntaje_jug2 + num_aleatorio_J2_1
    elif operacionJ2 == 2: #restar
        puntaje_jug2 = puntaje_jug2 - num_aleatorio_J2_1
elif usar == 2: #no usar
    if operacionJ2 == 1: #sumar
        penalizacionJ2 = penalizacionJ2 + num_aleatorio_J2_1
    elif operacionJ2 == 2: #restar
        penalizacionJ2 = penalizacionJ2 - num_aleatorio_J2_1
### FIN INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO

### INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO
usar = int(input("\nJugador 2, ¿Deseas usar el segundo número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
#ATENCIÓN: si el usuario no ingresa 1 0 2 el programa no funcionará
if usar == 1: #usar
    if operacionJ2 == 1: #sumar
        puntaje_jug2 = puntaje_jug2 + num_aleatorio_J2_2
    elif operacionJ2 == 2: #restar
        puntaje_jug2 = puntaje_jug2 - num_aleatorio_J2_2
elif usar == 2: #no usar
    if operacionJ2 == 1: #sumar
        penalizacionJ2 = penalizacionJ2 + num_aleatorio_J2_2
    elif operacionJ2 == 2: #restar
        penalizacionJ2 = penalizacionJ2 - num_aleatorio_J2_2
### FIN INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO

### INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO
usar = int(input("\nJugador 2, ¿Deseas usar el tercer número aleatorio? \nIngresa 1 para Sí o 2 para No: "))
#ATENCIÓN: si el usuario no ingresa 1 0 2 el programa no funcionará
if usar == 1: #usar
    if operacionJ2 == 1: #sumar
        puntaje_jug2 = puntaje_jug2 + num_aleatorio_J2_3
    elif operacionJ2 == 2: #restar
        puntaje_jug2 = puntaje_jug2 - num_aleatorio_J2_3
elif usar == 2: #no usar
    if operacionJ2 == 1: #sumar
        penalizacionJ2 = penalizacionJ2 + num_aleatorio_J2_3
    elif operacionJ2 == 2: #restar
        penalizacionJ2 = penalizacionJ2 - num_aleatorio_J2_3
### FIN INICIO DEL DEL BLOQUE QUE SE REPITE POR CADA NÚMERO

print("El jugador 1 queda con los siguientes puntajes:\n")
print("EL jugador 2 queda con los siguientes puntajes:\n")
print("Puntaje jugador 1: ", puntaje_jug1)
print("Puntaje Jugador 2: ", puntaje_jug2)
print("Penalización Jugador 1: ", penalizacionJ1)
print("Penalización Jugador 2: ", penalizacionJ2)
