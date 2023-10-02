# Escribir un programa que pida dos números enteros y que calcule su división. El
# programa deberá indicar si la división es exacta o no.

a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese otro numero entero"))

div = a/b
print("El resultado es", div)
if a%b == 0:
    print("La division es exacta")
else:
    print("La division no es exacta")