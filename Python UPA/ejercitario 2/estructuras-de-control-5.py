# Escribir un programa que lea un número desde el teclado e informe por pantalla si
# es positivo, negativo o igual a cero.
a = int(input("Ingrese un numero"))
if a>0:
    print("El numero es positivo")
elif a<0:
    print("El numero es negativo")
elif a==0:
    print("El numero es igual a cero")