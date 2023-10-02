# Escribir un programa que permita la carga de una matriz 3x3. El programa
# deberá trasponer la matriz y luego imprimir la matriz traspuesta.
import random

matriz = []
filas = 3
columnas = 3
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input("ingrese un numero"))
        fila.append(valor)
    matriz.append(fila)
for fila in matriz:
    for valor in fila:
        print(valor, end="  ")
    print()

matriz_res = []
for i in range(filas):
    fila_res = []
    for j in range(columnas):
        valor = matriz[j][i]
        fila_res.append(valor)
    matriz_res.append(fila_res)

print("La matriz traspuesta es: ")
for fila_res in matriz_res:
    print(fila_res)

"""
matriz_res = []
for i in range(filas,0,-1): # Forma de imprimir inversa (Del num mas grande al mas chico)
    fila_res = []
    for j in range(columnas,0,-1):
        valor = matriz[i-1][j-1]   # Sentido contrario de imprimir matriz
        fila_res.append(valor)
    matriz_res.append(fila_res)
"""