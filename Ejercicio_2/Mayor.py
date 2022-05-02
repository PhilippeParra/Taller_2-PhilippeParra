"""Ejercicio No. 2
de 3 numeros de devuelve el mayor"""

print("----------------------------------------")
print("--------------NUMERO MAYOR--------------")
print("----------------------------------------")


#input

X = int(input("Digite el primer numero: "))
Y = int(input("Digite el segundo numero: "))
Z = int(input("Digite el tercer numero: "))

#processing

if X > Y and X > Z:
    mayor = X    
    
if Y > X and Y > Z:
    mayor = Y

if Z > X and Z > Y:
    mayor = Z

#output
print("el numero mayor entre \n" + str(X) + "\n" + str(Y) + "\n" + str(Z) + "\nEs:" + str(mayor))