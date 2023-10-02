# 2 jugadores, cada uno tiene 2 dados.
# como almacenar los valores en la matriz
# los valores de los dados deben de ser almacenados en una matriz
import random
valor_dado_jugador1 = 0
valor_dado_jugador2 = 0
dado = random.randint(1,6)
dado2 = random.randint(1,6)
turno = 0

matriz = []
filas = 3 # Parte horizontal de la matriz
columnas = 3 # Parte vertical de la matriz
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = dado
        fila.append(valor)
    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="  ")
    print()
