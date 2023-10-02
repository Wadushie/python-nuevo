# Escribir un programa que permita a dos personas jugar el juego de sumar 15. La suma será
# obtenida de manera aleatoria para cada jugador. Cada jugador deberá contar con una variable que
# almacene la suma de los números obtenidos. A continuación, las reglas del juego:
# 1. El programa deberá generar tres números aleatorios para cada jugador.
# 2. Los números generados estarán en el rango de 1 a 10.
# 3. El jugador deberá indicar los números a utilizar. (puede utilizar 1, 2 o los tres números
# generados)
# 4. El programa deberá sumar los números indicados por cada jugador.
# 5. El jugador que más se acerque a 15 será el ganador.
import random

#jugador 1
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)
num3= random.randint(1, 10)
# Suma de numeros
sum1 = num1
sum2 = (num1+num2)
sum3 = (num1+num2+num3)
# jugador 2
num4 = random.randint(1, 10)
num5 = random.randint(1, 10)
num6= random.randint(1, 10)
# Suma de numeros 2
sum4 = num4
sum5 = (num4+num5)
sum6 = (num4+num5+num6)

# Seleccion de numeros
opcion = int(input("Entre los 3 numeros generados aleatoriamente, quieres usar solo 1, o 2 o los 3 numeros?"))
if opcion ==1:
    print("Se utilizará un solo numero: ", sum1)
elif opcion ==2:
    print("Se utilizará 2 numeros: ", sum2)
elif opcion ==3:
    print("Se utilizará 3 numeros: ", sum3)

opcion2 = int(input("Entre los 3 numeros, quieres usar solo 1, o 2 o los 3?"))
if opcion2 == 1:
    print("Se utilizará un solo numero: ", sum4)
elif opcion2 == 2:
    print("Se utilizará 2 numeros: ", sum5)
elif opcion2 == 3:
    print("Se utilizará 3 numeros: ", sum6)

# Guia para saber el ganador
if sum1 > 0 and sum1 <= 15:
    print("El jugador 1 gana por mayoria de puntos", sum1)
elif sum2 > 0 and sum2 <= 15:
    print("El jugador 1 gana por mayoria de puntos", sum2)
elif sum3 > 0 and sum3 <= 15:
    print("El jugador 1 gana por mayoria de puntos", sum3)

if sum4 > 0 and sum4 <= 15:
    print("El jugador 1 gana por mayoria de puntos", sum4)
elif sum5 > 0 and sum5 <= 15:
    print("El jugador 1 gana por mayoria de puntos", sum5)
elif sum6 > 0 and sum6 <= 15:
    print("El jugador 1 gana por mayoria de puntos", sum6)
