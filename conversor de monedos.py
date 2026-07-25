#convertidor de monedas 
cantidad= float(input("cantidad en mxn:"))
print("monedas: 1.USD 2EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
opcion= int(input("elige una opcion:"))
match opcion:
    case 1:
        resultado= cantidad /16.5
        moneda= "USD"
        print("el cambio es : ",resultado,moneda)
    case 2:
        resultado= cantidad /18.0
        moneda= "EUR"
        print("el cambio es : ",resultado,moneda)
    case 3:
        resultado= cantidad /0.45
        moneda= "THB"
        print("el cambio es : ",resultado,moneda)
    case 4:
        resultado= cantidad /0.12
        moneda= "JPY"
        print("el cambio es : ",resultado,moneda)
    case 5:
        resultado= cantidad/0.013
        moneda= "KRW"
        print("el cambio es : ",resultado,moneda)
    case 6:
        resultado= cantidad /11.5
        moneda= "AUD"
        print("el cambio es : ",resultado,moneda)
    case 7:
        resultado= cantidad /2.8
        moneda= "PEN"
        print("el cambio es : ",resultado,moneda)
    case 8:
        resultado= cantidad /8.2
        moneda= "CAD"
        print("el cambio es : ",resultado,moneda)
    case 9:
        resultado= cantidad /0.0023
        moneda= "VES"
        print("el cambio es : ",resultado,moneda)
    case 10:
        resultado= cantidad /0.046
        moneda= "ARS"
        print("el cambio es : ",resultado,moneda)
    case _:
        print("opcion no valida")
        resultado= None 
       