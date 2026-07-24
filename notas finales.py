#calculadora de nota final con validacion de rango
parcial = float(input("nota parciales del 0 al 100: "))
proyecto = float(input("nota proyecto del 0 al 100: "))
examen = float(input("nota examen del 0 al 100: "))
if 0 <= parcial <= 100 and 0 <= proyecto <= 100 and 0 <= examen <= 100:
    nota_final = (parcial * 0.3) + (proyecto * 0.4) + (examen * 0.3)
    print("La nota final es:", nota_final)
else:
    print("Error: Las notas deben estar en el rango de 0 a 100.")