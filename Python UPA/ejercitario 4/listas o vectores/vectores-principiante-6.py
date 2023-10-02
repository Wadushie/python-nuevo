# Leer 10 valores ingresados por el usuario y almacenarlos en un vector. Luego
# imprimir el mayor valor del vector.
vec = []
vec2 = []
mayor_actual = 0
for i in range(10):
    num = int(input("Ingrese un valor: "))
    vec.append(num)
print("Los valores dentro del vector son: ",vec)

mayor_actual = vec[0]
for numero_de_la_lista in vec:
    if  numero_de_la_lista > mayor_actual:
        mayor_actual = numero_de_la_lista
print("El numero de mayor valor es: ", mayor_actual)
