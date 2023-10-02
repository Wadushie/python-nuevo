# Escribir un programa que guarde 10 valores numéricos en una lista y luego
# imprima los valores guardados.
vec = []
for x in range(10):
    num = int(input("Ingrese un valor numerico"))
    vec.append(num)
print("Los valores guardados son: ",vec)