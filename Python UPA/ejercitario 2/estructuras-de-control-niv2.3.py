# Escribir un programa que pida al usuario una hora en hora:minutos:segundos (se
# pueden leer en tres variables separadas) y diga la hora que es un segundo después.
hora = int(input("Dame la hora: "))
min = int(input("Dame los minutos: "))
seg = int(input("Dame los segundos: "))

print("El tiempo es: ",hora,min,seg)
seg = seg+1
if seg > 59:
    min = min +1
    seg = 0
    if min > 59:
        hora = hora+1
        min = 0
        if hora == 24:
            hora = 00
print("El nuevo tiempo es: ", hora,min,seg)
