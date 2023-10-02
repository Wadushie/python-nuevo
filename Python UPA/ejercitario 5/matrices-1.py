# Como crear un a matriz
matriz = []
filas = int(input("Ingrese el número de filas de la matriz: ")) # Parte horizontal de la matriz
columnas = int(input("Ingrese el número de columnas de la matriz: ")) # Parte vertical de la matriz
#Carga la matriz
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor para la posición [{i+1}][{j+1}]: "))
        fila.append(valor)
    matriz.append(fila)
        #Imprime la matriz
for fila in matriz:
    for valor in fila:
        print(valor, end=" ")
    print(  )
