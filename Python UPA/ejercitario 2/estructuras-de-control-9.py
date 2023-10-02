# Escribir un programa que pida dos números enteros y que escriba si el mayor es
# múltiplo del menor.
a = int(input("Ingrese un numero"))
b = int(input("Ingrese otro numero"))

if a > b:
    resto =a%b
    if resto == 0:
        print("El resto es igual a 0")
    else: print("El resto no es igual a 0")
