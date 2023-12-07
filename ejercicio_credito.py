#ingreso de datos
edad = int(input("Ingresa tu edad: "))
sistema_financioero = int(input("Años de antiguedad en sistema financiero: "))
ingreso = float (input ("Ingreso salarial: "))

#evaluacion de condiciones
a = edad >= 18
b = sistema_financioero > 3 and ingreso > 2.500
c = ingreso > 4.000

validar = a and (b or c)

#validar
if validar:
    print ("crédito aprobado")
else:
    print ("Crédito no aporbado")

    