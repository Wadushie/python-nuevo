#Suponiendo que 1 euro = 1.33250 dólares. Escribe un programa que pida al usuario
#un número de dólares y calcule el cambio en euros.
dolar = int (input("Ingrese la cantidad de dolares que quiera pasar a euros"))
# nombre = int (input)) --> Esto es para convertir la entrada a un numero
dolarcambio = 1.33250
print("El cambio actual es de 1.33250 dolares al euro")
cambio = dolar / dolarcambio
print("El cambio a euro es de: ", cambio)
