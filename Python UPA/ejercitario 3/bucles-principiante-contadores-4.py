# Escriba un programa que imprima la tabla de multiplicar del 5 y del 8.
i =int(input("Ingrese un numero"))

for cont in range(1,10):
    mult = i * cont
    print("La tabla de multiplicar es: ", i, "*", cont, "=", mult)