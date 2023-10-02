# Escribir un programa para leer 10 números y mostrarlos en orden inverso al
# introducido.
vec = []
vec2 = []
for x in range(10):
    num = int(input("Ingrese un numero"))
    vec.append(num)
print("El vector orden normal es: ", vec)
for x in range(9,-1,-1):
    print("El vector de orden inverso es: ",vec[x])

# Para la segunda forma de impresion, se debe de declarar otro vector, (vec2) para que muestre en forma inversa
for x in range(10,0,-1):    # Forma de impresion inversa
    vec2.append(x)
print("El vector de orden inverso es (Forma 2 de demostracion): ",vec2)