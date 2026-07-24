#clasificacion de calificaciones
calificacion = float(input("ingrese su calificacion del 0 al 100: "))
if calificacion >= 90:
    print("A")
elif calificacion >= 80:
    print("B")
elif calificacion >= 70:
    print("C")
elif calificacion >= 60:
    print("D")
else:
    print("F")
    print ("tu calificacion es:", calificacion)