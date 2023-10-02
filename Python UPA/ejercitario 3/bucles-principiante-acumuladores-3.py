# Escriba un programa que solicite números enteros hasta que se introduzca 0. El
# programa deberá imprimir la cantidad de números positivos y la cantidad de números
# negativos leídos.
num = 1
numposit = 0
numnegat = 0
while num != 0:
    print("Ingrese un numero entero")
    num = int(input())
    if num > 0:
        numposit = numposit + 1
    elif num < 0:
        numnegat = numnegat + 1
    if num == 0:
        break
print("Los numeros positivos son:", numposit, "Y los numeros negativos son: ",numnegat)
