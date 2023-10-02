# Escribir un programa que lea un vector de 10 números enteros. Obtener la suma
# de todos ellos y la media.
vec = []
suma = 0
for i in range(10):
    num = int(input("Ingrese un numero"))
    vec.append(num)
print("Los valores del vector son: ", vec)

# suma directa de valores de un vector
suma2 = sum(vec)
print("Los valores dentro del vector son: ",suma2)

# suma de valores de un vector en un ciclo for
for num in vec:
    suma = suma + num
print("La suma de los valores del vector son: ",suma)