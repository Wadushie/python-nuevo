#Escribir un programa que permita leer un número y determine cuántos años,
#meses y días contiene el número leído.
numdias = int(input("Ingrese el numero de dias a ser calculado"))
print("Son ", numdias, " dias")

anhos = (numdias//365)
print("Los años restantes son: ", anhos)

mes = ((numdias - anhos*365)//30)
print("Los meses restantes son: ", mes)

dias = ((numdias - anhos*365)%30)
print("Los dias restantes son: ", dias)