# Dado un texto t, determinar cuántas consolantes aparecen en el mismo.
texto = input('Ingrese una frase o palabra: ')
consonantes = "bcdfghjklmñpqrstvwxyzBCDFGHJKLMÑPQRSTVWXYZ"
j = 0
for i in texto:
    if i in consonantes:
        j = j + 1
print(f"La frase [{texto}] tiene {j} consonantes.")
