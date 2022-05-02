"""Ejercicio No. 8
Resolver una ecuacion de Segundo grado."""

print("-----------------------------------------------")
print("------------------ax^2+bx+c=0------------------")
print("-----------------------------------------------")

import math


a = input("Digite A: ")
a = float(a)

b = input("Digite B: ")
b = float(b)

c = input("Digite C: ")
c = float(c)

if a != 0:
    if b != 0:
        if (b*b)-(4*a*c) >= 0:
            x1 = (-(b)) + math.sqrt(((b*b)-(4*(a)*(c)))) / (2*(a))
            x1 = float(x1)
            x2 = (-(b)) - math.sqrt(((b*b)-(4*(a)*(c)))) / (2*(a))
            x2 = float(x2)
            print("X1 = " + str(x1))
            print("X2 = " + str(x2))
        else:
            print("X no existe")
    else:
        print("X no existe")
else:
    print("X no existe")