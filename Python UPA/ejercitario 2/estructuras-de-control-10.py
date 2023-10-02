# Escribe un programa que pida al usuario la velocidad de un vehículo. Si la velocidad
# es menor a 20, imprimir “Muy Despacio”; si la velocidad es mayor a 80, imprimir
# “Muy rápido”. En otro caso imprimir “Velocidad correcta”.
a = int(input("Ingrese el valor de velocidad"))
if a <20:
    print("La velocidad promedio es menor a 20")
elif a >80:
    print("La velocidad es muy rapida")
else:
    print("Velocidad Correcta")
