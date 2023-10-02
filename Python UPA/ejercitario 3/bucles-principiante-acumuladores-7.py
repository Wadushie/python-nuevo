# Escribir un programa que cuente la cantidad de números múltiplos de 7 que hay entre
# 30 y 70.
contador_de_numeros_multiplos7 = 0
num = 0
for num in range(30,70):
    if num % 7 == 0:
        contador_de_numeros_multiplos7 = contador_de_numeros_multiplos7 + 1
        print("Los numeros multiplos de 7 son: ", num)
print("la cantidad de numeros multiplos son: ",contador_de_numeros_multiplos7)
