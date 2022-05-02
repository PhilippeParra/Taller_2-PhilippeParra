"""Ejercicio No. 5 
dado un numero entero determinar si su ultimos dos digitos son iguales."""

print("---------------------------------------------")
print("---------------ULTIMOS IGUALES---------------")
print("---------------------------------------------")

X = int(input("Digite su numero: "))

X1 = X % 100
X1 = int(X1)

X2 = X1 / 10
X2 = int(X2)

X3 = X % 10
X3 = int(X3)

if X2 == X3 and 10 <= X:
    print("Los dos ultimos digitos del numero dado son iguales")