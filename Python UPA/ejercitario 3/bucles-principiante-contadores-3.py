# Escriba un programa que solicite un número positivo y luego imprima los 30
# números posteriores al número leído.
n = int(input("Ingrese un numero positivo"))
while n > 0 and n < 30:
    n = n + 1
    print("Los numeros posteriores al numero ingresado son: ",n)

num = int(input("Introduzca el numero"))
for cont in (range(30)):
    x = num + cont
    print("Los numeros posteriores al ingresado son: ",x)