# Escribir un programa que imprima los valores de una lista con 10 elementos.
# si se declara al vector así, se le puede modificar los valores con el vec.append(int contador)
vec = []
for x in range(10):
    num = int(input("Ingrese un numero"))
    vec.append(num) # Carga en el vector los numeros que se dan
print(vec)  # imprimen el vector con los numeros ingresados