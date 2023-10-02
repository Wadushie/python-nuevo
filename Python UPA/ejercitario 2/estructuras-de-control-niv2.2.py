# Escribe un programa que pida al usuario un entero para el día actual de la semana
# (Domingo es 0, Lunes es 1, ..., Sábado es 6). También pedir al usuario al usuario el
# número de días posteriores a hoy e imprimir el futuro día de la semana. Por
# ejemplo: si hoy es martes (2) y el usuario ingresa 5. El futuro día sería domingo.
# Nivel Intermedio
elec = int(input("Ingrese del 0 al 6 para saber el dia actual"))

if elec==0:
    print("El dia de hoy es Domingo, ")
elif elec==1:
    print("El dia de es hoy es Lunes")
elif elec==2:
    print("El dia de es hoy es Martes")
elif elec==3:
    print("El dia de es hoy es Miercoles")
elif elec==4:
    print("El dia de es hoy es Jueves")
elif elec==5:
    print("El dia de es hoy es Viernes")
elif elec==6:
    print("El dia de es hoy es Sabado")

sum = int(input("Cuantos dias quedan a futuro?"))
total = elec + sum
total = total % 7
print("El dia a futuro será: ",total)
if total == 0:
    print("El día a futuro será Domingo.")
elif total == 1:
    print("El día a futuro será Lunes.")
elif total == 2:
    print("El día a futuro será Martes.")
elif total == 3:
    print("El día a futuro será Miércoles.")
elif total == 4:
    print("El día a futuro será Jueves.")
elif total == 5:
    print("El día a futuro será Viernes.")
elif total == 6:
    print("El día a futuro será Sábado.")