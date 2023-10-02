# Escribir un programa que permita el rellenado de una matriz 7x7 de tal forma
# que los elementos de la diagonal principal sean 1 y todos los demás elementos
# sean 0.

matriz = []
filas = 7
columnas = 7
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = 0
        fila.append(valor)
    matriz.append(fila)
for fila in matriz:
    for valor in fila:
        print(valor, end="  ")
    print()
print("------------")
for i in range(filas):
    matriz[i][i] = 1

for i in range(filas,0,-1):
    matriz[filas-i][i-1] = 1

for fila in matriz:
    for valor in fila:
        print(valor, end="  ")
    print()
