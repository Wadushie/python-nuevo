# Escriba un programa que permita la lectura de 20 números enteros e imprima cuántos
# de estos números son negativos.
num = 1
cantidad = 20
numposit = 0
numnegat = 0
for num in range(cantidad):
    print("Ingrese un numero entero")
    num = int(input())
    if num > 0:
        numposit = numposit + 1
    elif num < 0:
        numnegat = numnegat + 1
print("Los numeros positivos son:", numposit, "Y los numeros negativos son: ", numnegat)