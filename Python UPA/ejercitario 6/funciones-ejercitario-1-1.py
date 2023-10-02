def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def fraction(a, b):
    global str
    if (b % a) == 0:    # revisa si los numreos son divisibles
        my_a = 1
        my_b = int(b/a)
    else:
        my_d = a
        my_cd = 1
        while my_d > 1:
            print('Recorrido:' + str(my_d))
            if ((a%my_d == 0) and (b%my_d==0)):
                print('Divisor Comun:' + str(my_d))
                my_cd = my_d
                break
            my_d -= 1
        my_a = int(a/my_cd)
        my_b = int(b/my_cd)
    return 'Fraction:' + str(my_a) + '/' + str(my_b)    # si el mcd es divisible
    # caso indirecto buscar
def fractionadd(a, b):
        split_a = a.split('/')
        split_b = b.split('/')
        my_a=int(split_a[0])
        my_ad=int(split_a[1])
        my_b=int(split_b[0])
        my_bd=int(split_b[1])
        # multiplo comun de ad y bd
        my_cd = my_ad * my_bd
        my_ac = my_a * my_bd
        my_bc = my_b * my_ad
        # suma convertido a nueva base multiplo comun, suma numerador y imprime
        my_r = my_ac + my_bc
        my_rd = my_cd
        print('Cadena :' + a +' , '+ b)
        print('Numerador : ' +str(my_a))
        print('Denominador : ' +str(my_ad))
        print('Numerador : ' +str(my_b))
        print('Denominador : ' +str(my_bd))
        print('Denominador Comun: ' +str(my_cd))
        print('Cadena :' + a + ' , ' + b)
        print('Numerador : ' + str(my_a))
        print('Denominador : ' + str(my_ad))
        print('Numerador : ' + str(my_b))
        print('Denominador : ' + str(my_bd))
        print('Denominador Comun: ' + str(my_cd))
        print('Cadena : ' + str(my_ac) + '/' + str(my_cd) + ' , ' + str(my_bc) + '/' + str(my_cd))
        print('Resultado : ' + str(my_r) + '/' + str(my_rd))
        return 'Resultado : ' + str(my_r) + '/' + str(my_rd)
def getArithmeticOperation(operation):
    if operation==1:
        return add
    elif operation==2:
        return subtract
    elif operation==3:
        return multiply
    elif operation==4:
        return fraction
    elif operation==5:
        return fractionadd

while True:
    print('Arithmetic Operations')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Fraction')
    print('5. Fraccionadd')
    print('0. Exit')
    operation = int(input('Enter the arithmetic operation : '))
    if(operation==0):
        break
    func = getArithmeticOperation(operation)
    if(operation == 5):
        a = (input('Enter a : '))
        b = (input('Enter b : '))
    else:
        a = int(input('Enter a : '))
        b = int(input('Enter b : '))
    result = func(a, b)
    print('The result is :', result)
