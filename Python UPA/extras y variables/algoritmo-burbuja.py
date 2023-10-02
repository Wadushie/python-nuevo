# realizar un algoritmo burbuja que se ordene
import random
from time import clock
from os import system as sys
import random
vector = [random.randint(1,10000)]
def burbuja(valores):
    nuevo = valores[:]
    for i in range(len(nuevo)):
        for j in range(len(nuevo) - 1 - i):
            if nuevo[j] > nuevo[j + 1]:
                nuevo[j], nuevo[j + 1] = nuevo[j + 1], nuevo[j]
print(" largo", "\t\t", "tiempo")
print ("==============================")
sys('sort  -nk1 timer.txt > tiempo.txt')

