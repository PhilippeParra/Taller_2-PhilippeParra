"""Ejercicio No. 7
Resolver una ecuacion de primer grado."""

print("----------------------------------------------")
print("------------------ax + b = c------------------")
print("----------------------------------------------")


a = input("Digite A: ")
a = float(a)

b = input("Digite B: ")
b = float(b)

c = input("Digite C: ")
c = float(c)


if a != 0:
    if b != 0:
        x = (c + (b*(-1)))/a
        print("X = " + str(x))
    else:
        print("X = 0")
else: 
    print("X no existe")