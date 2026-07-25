#brindar informacion
consulta = input("Ingrese nombre de artista, pelicula o serie: ").lower()
match consulta:
    case "inception":
        info="pelicula de ciencia ficcion dirigida por christopher nolan."
        print("informacion",info)
    case "the beatles":
        info="banda de rock britanica formada en 1960."
        print("informacion",info)
    case "rick and morty":
        info="serie animada de ciencia ficcion creada por justin roiland y dan harmon."
        print("informacion",info)
    case "stranger things":
        info="serie de ciencia ficcion y terror creada por los hermanos duffer."
        print("informacion",info)
    case "avengers":
        info="pelicula de superhéroes basada en los personajes de marvel comics."
        print("informacion",info)
    case _:
        info= "no se encontro informacion"
        print("informacion",info)