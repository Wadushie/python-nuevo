# Escribe una función reciba dos paramentos independientes, el numerador y
# denominador de una fracción de números enteros. La función debe imprimir la
# fracción simplificada.
# hacer una operacion mcd
def mcd(a, b):
    if b == 0:
        return a
    return mcd(b, a % b)
def fraccion(denom,numer):
    denom = int(input("Ingrese el denominador"))
    numer = int(input("Ingrese el numerador"))
    return numer, denom
