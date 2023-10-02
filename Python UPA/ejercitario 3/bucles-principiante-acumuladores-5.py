# Escriba un programa que solicite números enteros hasta que se introduzca 0. El
# programa deberá imprimir la suma de todos los números positivos.
num = int
numposit = 0
sumtotal = 0
while num != 0:
    print("Ingrese un numero entero")
    num = int(input())
    if num > 0:
        numposit = numposit + num
print("Los numeros positivos son:", numposit)