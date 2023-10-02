# Escribir un programa que permita la carga de dos matrices 3x3. El programa
# deberá imprimir la suma de ambas matrices.
    # Matriz 1
matriz = []
filas = 3 # Parte horizontal de la matriz
columnas = 3 # Parte vertical de la matriz
for i in range(filas):
    fila = []
    for j in range(columnas):
        print(f"Ingrese un numero dentro de la matriz [{i}] [{j}]")
        valor = int(input())
        fila.append(valor)
    matriz.append(fila)

for fila in matriz:
    for valor in fila:
        print(valor, end="  ")
    print()
    # Matriz 2
matriz2 = []
filas2 = 3
columnas2 = 3
for i in range(filas2):
    fila2 = []
    for j in range(columnas2):
        print(f"Ingrese un numero que sera almacenado dentro de la matriz [{i}] [{j}]")
        valor2 = int(input())
        fila2.append((valor2))
    matriz2.append(fila2)
for fila2 in matriz2:
    for valor2 in fila2:
        print(valor2, end=" ")
    print()
    # Matriz Resultante
matriz_resul = []
filas_resul = 3
columnas_resul = 3
for i in range(filas_resul):
    fila_resul = []
    for j in range(columnas_resul):
        suma = matriz[i][j] + matriz2[i][j]
        fila_resul.append(suma)
    matriz_resul.append(fila_resul)

print("La matriz resultante es: ")
for filas_resul in matriz_resul:
    print(filas_resul)
    # Metodo 2 de imprimir una matriz
