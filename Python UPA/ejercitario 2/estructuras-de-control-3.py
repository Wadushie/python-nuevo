# Escribir un programa que solicite dos números desde el teclado e informe si el
# primero es mayor y en ese caso reste el 2o del 1o, o informe si el primero es menor
# y en ese caso los sume, o informe si el primero es igual al segundo y en ese caso los
# multiplique para mostrar el resultado.
a = int(input("Ingrese un numero"))
b = int(input("Ingrese otro numero"))

if a > b:
    print("El primer numero ingresado: ", a, " es mayor que el segundo: ", b)
    res = a-b
    print("El resultado de la resta es: ", res)
elif b > a:
    sum = b+a
    print("El resultado de la suma es: ", sum)
    print("El segundo numero ingresado: ", b, " es mayor que el primero: ", a)
elif a == b:
    multi = a * b or b * a
    print("Los numeros ingresados son iguales")
    print("El resultado de la multiplicacion es", multi)