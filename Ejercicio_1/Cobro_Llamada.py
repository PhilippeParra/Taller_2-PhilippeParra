"""Ejercicio No. 3 Cobro por llamada telefonica."""

print("---------------------------------------------")
print("-------------Cobro Por Minutos---------------")
print("---------------------------------------------")

#input
minutos = int(input("Digite el tiempo de llamada en minutos: "))

#processing
if minutos <= 3:
    Z = 300

else: 
    Z = (minutos - 3) * 50 + 300

#output
print("El costo de una llamada de " + str(minutos) + " minutos es de " + str(Z))
