# Listar los numeros del 1 al 100 de 5 en 5
n = int(input("Ingrese un numero: "))
for x in range(1,101):
    mult = n * (x*5)
    print("La lista de 5 en 5 es: ",n, "*", x*5, "=",mult)