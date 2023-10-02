# Calcular la suma de los primeros 10 números múltiplos de 5.
suma = 0
contador = 0
cantidad_numeros_multiplos_de_5 = 0
num = 0
while cantidad_numeros_multiplos_de_5 < 10:
    num = num + 1
    if num % 5 == 0:
        print("Los numeros multiplos de 5 son: ", num)
        cantidad_numeros_multiplos_de_5 = cantidad_numeros_multiplos_de_5 + 1
        suma = suma + num
print("La suma de los multiplos son: ", suma)