# Escribir un programa que lea una cadena e imprima en pantalla la cantidad de vocales,
# consonantes, espacios en blanco y dígitos que tiene la cadena.
def cadenas(cadena):
    vocales = 'aeiouAEIOU'
    j = 0
    for i in cadena:
        if i in vocales:
            j = j + 1
    #print("La frase ", cadenas, " tiene ", j, " vocales")
    return j
print(f"La cantidad de vocales son: {j}")