#convertidor de temperatura
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
print("1. fahrenheit\n2. kelvin")
opcion = int(input("elige una opcion:"))
match opcion:
    case 1:
        fahrenheit = (celsius * 9/5) + 32
        print("La temperatura en grados Fahrenheit es:", fahrenheit)
    case 2:
        kelvin = celsius + 273.15
        print("La temperatura en grados Kelvin es:", kelvin)
    case _:
        print("Opción no válida.")