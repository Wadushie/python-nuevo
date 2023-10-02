# Escriba un programa que solicite números enteros hasta que se introduzca 0. El
# programa deberá imprimir la cantidad números leídos.
num = int
suma = 0
while num != 0:
    print("Ingrese el numero a sumar")
    num = int(input())
    suma = suma + num
    if num == 0:
        break
print("La suma es: ", suma)