# Dado un texto t, determinar cuántas vocales aparecen en el mismo.
cadena = input('Ingrese la frase a analizar')
vocales = 'aeiouAEIOU'
j = 0
for i in cadena:
    if i in vocales:
        j = j + 1
print("La frase ", cadena, " tiene ", j, " vocales")