# 8. Escriba un programa que pida dos números enteros y escriba la suma de todos los
# enteros desde el primer número hasta el segundo.
n1 = int(input("Ingrese un num"))
n2 = int(input("Ingrese otro num"))
guardar = 0
for i in range(n1,n2):
    if i %2 ==0:
        print(i)
        guardar = guardar + i
    #else:
       # print("El numero no es entero")
print("La suma es: ", guardar)