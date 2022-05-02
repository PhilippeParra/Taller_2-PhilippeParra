"""Ejercicio No. 3
de un numero dado se identifica si es positivo de 4 digitos"""

print("----------------------------------------------")
print("--------------POSITIVO-4-DIGITOS--------------")
print("----------------------------------------------")


X = int(input("Digite su numero: "))
if 1000 <= X <= 9999:
    print("Su numero es positivo y de 4 digitos.")
