# Escribir un programa que lea valores para dos variables y calcule la suma, resta,
# multiplicación y división entre ambas (validar la división por cero).
print("Operaciones")
print("1 = Suma")
print("2 = Resta")
print("3 = Multiplicacion")
print("4 = Division")
cont = int(input("Elija un numero para iniciar la operacion deseada"))

a = int(input("Ingrese un numero"))
b = int(input("Ingrese otro numero"))
if cont==1:
    sum = a+b
    print("El resultado de la suma es: ", sum)
elif cont==2:
    res = a-b
    print("El resultado de la resta es: ", res)
elif cont==3:
    multi = a*b
    print("El resultado de la multiplicacion es: ", multi)
elif cont==4:
    div = a//b
    print("El resultado de la division es: ",div)