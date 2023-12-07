fecha = int(input("Ingrese su año de nacimiento:  "))

generacion_silenciosa = (1920, 1940) 
baby_boomer = (1946, 1964)
generacion_x = (1965, 1979)
genreacion_y = (1980, 2000)
genreación_z = (2001, 2010)

if fecha >= generacion_silenciosa[0] and fecha <= generacion_silenciosa[1]:
    print ("Perteneces a generacion silenciosa")
elif fecha >= baby_boomer[0] and fecha <= baby_boomer[1]:
    print ("Perteneces a la generacion baby boomer")
elif fecha >= generacion_x[0] and fecha <= generacion_x[1]:
    print ("Perteneces a generacion X")
elif fecha >= genreacion_y[0] and fecha <= genreacion_y[1]:
    print ("Perteneces a generacion Y")
elif fecha >= genreación_z[0] and fecha <= genreación_z[1]:
    print ("Perteneces a genreacion Z")
else:
    print ("No existe generación asociada")

