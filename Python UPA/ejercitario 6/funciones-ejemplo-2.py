# obtener media, promedio, maximo y minimo de la lista anterior
lista = [5,10,40,15]
def calcular_valores (lista):
    suma = sum (lista)
    promed = suma / len(lista)
    num_min = min(lista)
    num_max = max(lista)
    return promed, num_max, num_min
resultado = calcular_valores(lista)
print("El promedio de la lista es: ",resultado[0],"\nEl valor maximo dentro de la lista es: ", resultado[1],"\nEl valor minimo dentro de la lista es: ", resultado[2])
