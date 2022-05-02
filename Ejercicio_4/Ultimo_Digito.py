"""Programa para identificar de
un numero dado si su ultimo digito
es par"""

print("-----------------------------------------------")
print("---------¿Ultimo Digito Par?-------------")
print("-----------------------------------------------")

#input
X = int(input("digite el valor de X: "))

#processing

ultimo_digito = X % 10

Z = ultimo_digito % 2

if Z == 0:
    print("El ultimo digito de " + str(X) + " es PAR")

print("Eso era...")