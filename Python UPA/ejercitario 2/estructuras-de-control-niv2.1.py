# Escribir un programa que pida al usuario tres números y los imprima en orden
# decreciente.
# Nivel Intermedio
a = int(input("Ingrese un numero"))
b = int(input("Ingrese el segundo numero"))
c = int(input("ingrese el tercer numero"))
if a>b and a>c:
    if b>c:
        print("El orden es; ", a, b, c)
    else:
        print("El orden es: ",a ,c, b)
elif b>a and b>c:
    if a>c:
        print("El orden es: ", b, a, c)
    else:
        print("El orden es: ", b, c, a)
elif c>a and c>b:
    if a>b:
        print("El orden es: ", c, a, b)
    else:
        print("El orden es: ", c, b, a)