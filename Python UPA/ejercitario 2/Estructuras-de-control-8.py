# Escribir un programa que pida al usuario tres números y diga si la multiplicación
# de los dos primeros es igual al tercero.
a = int(input("Ingrese el primer numero"))
b = int(input("Ingrese el segundo numero"))
c = int(input("Ingrese el tercer numero"))
mult = a*b
if (mult) == c:
    print("La multiplicacion de los dos primeros numeros son iguales al tercero", c)
else:
    print("la multiplicacion no es igual al tercer numero", c)