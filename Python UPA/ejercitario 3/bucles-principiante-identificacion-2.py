# Escribe un programa que pregunte cuántos números se van a introducir. El programa
# deberá leer los números e imprimir los números leídos que son múltiplos de 5.
cant = int(input("Introduzca la cantidad de numeros que quiera usar"))
valorguardado = 0
nomultiplo = 0
contador_multiplo_5 = 1
for x in range(cant):
    x = x + 1
    num = int(input("Ingrese un numero"))
    if num % 5 == 0:
        num = contador_multiplo_5
        contador_multiplo_5 = contador_multiplo_5 + 1
        print("Los valores multiplos a 5 son: ",num)
    else:
        num = int(input("El numero no es multiplo de 5, Reintroduzca otro numero"))