nota = int(input("escribe tu nota: "))

match nota:
    case 0 | 1 | 2:
        print("muy deficiente")
    case 3 | 4:
        print("suspenso")
    case 5:
        print("aprobado")
    case 6:
        print("bien")
    case 7 | 8:
        print("notable")
    case 9:
        print("sobresaliente")
    case 10:
        print("matrícula de honor")