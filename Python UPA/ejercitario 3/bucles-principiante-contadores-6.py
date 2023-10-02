# Escriba un programa que pida dos números e imprima en pantalla todos los
# números comprendidos entre los números leídos.
lim1 = int(input("Ingrese un numero"))
n = int(input("Ingrese el limite que quiere dar a la funcion"))
cont = lim1
lim2 = n -1
while cont < lim2:
    cont = cont + 1
    print("Los numeros comprendidos son: ",cont)

