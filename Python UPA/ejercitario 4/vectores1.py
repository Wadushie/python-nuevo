vec = [3,5,7]   # Declarar un vector con los valores ya dentro
print(vec)  # imprime el vector

# Como cargar un vector dependiendo de su cantidad
contador = int(input("Ingrese cantidad de numeros a cargar"))
lista = []
for x in range(contador):
    num = int(input("Ingrese un numero"))
    lista.append(num)
print(lista)
