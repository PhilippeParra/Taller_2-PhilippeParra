"""Ejercicio No. 6
dado un numero entero determinar si la suma de sus ulimos dos digitos
es un numero de un digito."""

print("-----------------------------------------------")
print("---------SUMA DE LOS ULTIMOS 2 DIGITOS---------")
print("-----------------------------------------------")

X = int(input("Digite su numero: "))

X1 = X % 100
X1 = int(X1)

X2 = X1 / 10
X2 = int(X2)

X3 = X % 10
X3 = int(X3)

R = X2 + X3

if 0 < X2 + X3 <= 9:
    print("La suma de " + str(X2) + " y " + str(X3) + " da un numero de un digito el cual es " + str(R))