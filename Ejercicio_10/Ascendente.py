"""Ejercicio No. 10
de 3 numeros los devuelve en modo ascendente"""

print("----------------------------------------")
print("--------------ASCENDENTE----------------")
print("----------------------------------------")


#input

X = int(input("Digite el primer numero: "))
Y = int(input("Digite el segundo numero: "))
Z = int(input("Digite el tercer numero: "))

#processing

if X > Y:
    if Y > Z:
        print("El orden ascendente de los numeros dados es: \nMayor: " + str(X) + "\nMedio: " + str(Y) + "\nMenor: " + str(Z))
    else: 
        print("El orden ascendente de los numeros dados es: \nMayor: " + str(X) + "\nMedio: " + str(Z) + "\nMenor: " + str(Y))

if Y > X:
    if X > Z:
         print("El orden ascendente de los numeros dados es: \nMayor: " + str(Y) + "\nMedio: " + str(X) + "\nMenor: " + str(Z))
    else: 
        print("El orden ascendente de los numeros dados es: \nMayor: " + str(Y) + "\nMedio: " + str(Z) + "\nMenor: " + str(X))

if Z > X:
    if X > Y:
         print("El orden ascendente de los numeros dados es: \nMayor: " + str(Z) + "\nMedio: " + str(X) + "\nMenor: " + str(Y))
    else: 
        print("El orden ascendente de los numeros dados es: \nMayor: " + str(Z) + "\nMedio: " + str(Y) + "\nMenor: " + str(X))
