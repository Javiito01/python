dia = input("introduce un dia de la semana: ")

match dia:
    case "lunes" | "martes" | "miércoles" | "miercoles" | "jueves" | "viernes":
        print("Es un día laborable.")
    case "sábado" | "domingo":
        print("es fin de semana")
    case _:
        print("este dia no vale")