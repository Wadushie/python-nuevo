# Escribir un programa que lea un vector de 10 números enteros. El programa
# deberá mostrar por cada índice, el valor que se almacena.
# Ejemplo: [0] = 7, [1] = 12, etc.
vec = []
for i in range(10):
    num = int(input("Ingrese un numero"))
    vec.append(num)
for j in vec:
    print("Los valores dentro del vector son: ","[",j,"]")