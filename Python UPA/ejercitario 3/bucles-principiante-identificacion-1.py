# Escriba un programa que lea 20 números enteros e imprima el mayor número leído.
a = 0
valorguardado = 0
while a < 5:
    a = a+1
    cont = int(input("Ingrese un numero"))
    if cont > valorguardado:
        valorguardado = cont
print("El valor mayor es: ",valorguardado)