#calcular el precio con descuento
precio= float(input("ingrese el precio del producto: "))
if precio <= 100:
    descuento =0
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.20
else:
    descuento = 0.25

precio_con_descuento = precio - (precio * descuento)
print("El precio con descuento es:", precio_con_descuento)