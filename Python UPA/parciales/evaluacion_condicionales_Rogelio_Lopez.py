# Escribir un programa que permita a dos personas jugar el juego de sumar 15. La suma será
# obtenida de manera aleatoria para cada jugador. A continuación, las reglas del juego:
# 1. Cada jugador cuenta con dos variables: puntaje y penalización.
# 2. La variable puntaje deberá ser inicializada de manera aleatoria con un valor entre 1 y 20.
# 3. El programa deberá generar tres números aleatorios para cada jugador.
# 4. Los números generados estarán en el rango de 1 a 10.
# 5. El jugador deberá indicar los números a utilizar. (puede utilizar 1, 2 o los tres números
# generados)
# 6. El jugador deberá indicar la operación a realizar: sumar o restar.
# 7. El programa deberá tomar los números indicados por cada jugador y realizar la operación
# sobre la variable puntaje. Es decir, tomar los números indicados y sumar o restar del
# puntaje.
# 8. Los números no seleccionados se deberán sumar a la variable penalización.
# 9. El jugador ganador será el que tenga la suma más cercana a 15 y que tenga la menor
# penalización.
import random
def obtener_numero_aleatorio():
    return random.randint(1, 10)

def calcular_penalizacion(numero, seleccionados):
    return sum(seleccionados) - numero

# Función para el turno de un jugador
def turno_jugador(numero_jugador, puntaje_jugador, penalizacion_jugador):
    print(f"\nTurno del Jugador {numero_jugador}:")

    num1 = obtener_numero_aleatorio()
    num2 = obtener_numero_aleatorio()
    num3 = obtener_numero_aleatorio()

    print(f"Los números generados para el jugador {numero_jugador} son: {num1}, {num2}, {num3}")

    seleccionados = []
    operacion = input("Elija si quiere sumar o restar (sumar/restar): ")

    if operacion == "sumar":
        elec = int(input("Elija entre las opciones (1/2/3): "))

        if elec >= 1 and (sum(seleccionados) + num1) <= 15:
            seleccionados.append(num1)
        if elec >= 2 and (sum(seleccionados) + num2) <= 15:
            seleccionados.append(num2)
        if elec == 3 and (sum(seleccionados) + num3) <= 15:
            seleccionados.append(num3)

        suma = sum(seleccionados)
        puntaje_jugador += suma
        penalizacion_jugador += calcular_penalizacion(puntaje_jugador, seleccionados)
        print(f"Sumando: {suma}")

    elif operacion == "restar":
        elec = int(input("Elija entre las opciones (1/2/3): "))

        if elec >= 1 and (sum(seleccionados) + num1) <= 15:
            seleccionados.append(num1)
        if elec >= 2 and (sum(seleccionados) + num2) <= 15:
            seleccionados.append(num2)
        if elec == 3 and (sum(seleccionados) + num3) <= 15:
            seleccionados.append(num3)

        resta = sum(seleccionados)
        puntaje_jugador -= resta
        penalizacion_jugador += calcular_penalizacion(puntaje_jugador, seleccionados)
        print(f"Restando: {resta}")

    print(f"\nPuntaje del Jugador {numero_jugador}: {puntaje_jugador}, Penalización: {penalizacion_jugador}")

    return puntaje_jugador, penalizacion_jugador

# Función para jugar el juego
def jugar():
    jugador1 = input("Para jugar escriba 'iniciar' como jugador 1: ")

    # Inicialización de puntajes y penalizaciones
    puntaje_jugador1 = random.randint(1, 20)
    puntaje_jugador2 = random.randint(1, 20)
    penalizacion_jugador1 = 0
    penalizacion_jugador2 = 0

    print(f"El puntaje inicial del Jugador 1 es: {puntaje_jugador1}")
    print(f"El puntaje inicial del Jugador 2 es: {puntaje_jugador2}")

    if jugador1 == "iniciar":
        puntaje_jugador1, penalizacion_jugador1 = turno_jugador(1, puntaje_jugador1, penalizacion_jugador1)
        puntaje_jugador2, penalizacion_jugador2 = turno_jugador(2, puntaje_jugador2, penalizacion_jugador2)

        if abs(puntaje_jugador1 - 15) < abs(puntaje_jugador2 - 15):
            ganador = 1
        elif abs(puntaje_jugador1 - 15) > abs(puntaje_jugador2 - 15):
            ganador = 2
        else:
            if penalizacion_jugador1 < penalizacion_jugador2:
                ganador = 1
            elif penalizacion_jugador1 > penalizacion_jugador2:
                ganador = 2
            else:
                ganador = 0

        if ganador == 0:
            print("\n¡Es un empate!")
        else:
            print(f"\n¡El Jugador {ganador} ha ganado!")

if __name__ == "__main__":
    jugar()
