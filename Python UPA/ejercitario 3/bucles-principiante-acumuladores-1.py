# Escriba un programa que pregunte cuantos números se van a introducir, pida esos
# números y calcule su suma.
num1 = int(input("Ingrese la cantidad de numeros: "))
suma=0
for n in range(num1):
    print("Ingrese el numero que quiera sumar")
    num2 = int(input())
    suma = suma+num2

print("La suma de los numeros ingresados son: ",suma)