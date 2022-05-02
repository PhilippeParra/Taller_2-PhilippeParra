"""Ejercicio No. 9
De un precio base a pagar calcular segun las 
condiciones el total a pagar por el cliente."""

print("-------------------------------------------")
print("------------------NEGOCIO------------------")
print("-------------------------------------------")




total_a_pagar = input("Digite el valor base de la compra: ")
total_a_pagar = float(total_a_pagar)

C = int(input("El tipo de Cliente es \nGeneral(1) \no \nAfiliado(2)?: "))
print ("---------------------------------")

F = int(input("Formas de pago \nContado(1) \nPlazos(2) \nDigite la forma de pago: "))
print ("---------------------------------")

if C == 1:
    if F == 1:
        R = total_a_pagar - (total_a_pagar * 0.15)

        print("El total a pagar de " + str(total_a_pagar) + " pesos con un descuento del 15% es " + str(R) + " pesos")

    else: 
        R = total_a_pagar + (total_a_pagar * 0.1)

        print("El total a pagar de " + str(total_a_pagar) + " pesos con un recargo del 10% es " + str(R) + " pesos")
else: 
    if F == 1:
        R = total_a_pagar - (total_a_pagar * 0.20)

        print("El total a pagar de " + str(total_a_pagar) + " pesos con un descuento del 20% es " + str(R) + " pesos")

    else: 
        R = total_a_pagar + (total_a_pagar * 0.05)

        print("El total a pagar de " + str(total_a_pagar) + " pesos con un recargo del 5% es " + str(R) + " pesos")