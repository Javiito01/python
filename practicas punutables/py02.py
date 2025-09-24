dia = int(input("Escribe el día de tu cumpleaños: "))
mes = int(input("Escribe el mes de tu cumpleaños: "))

match mes:
    case 1:
        print("Capricornio" if dia < 20 else "Acuario")
    case 2:
        print("Acuario" if dia < 19 else "Piscis")
    case 3:
        print("Piscis" if dia < 21 else "Aries")
    case 4:
        print("Aries" if dia < 20 else "Tauro")
    case 5:
        print("Tauro" if dia < 21 else "Géminis")
    case 6:
        print("Géminis" if dia < 21 else "Cáncer")
    case 7:
        print("Cáncer" if dia < 23 else "Leo")
    case 8:
        print("Leo" if dia < 23 else "Virgo")
    case 9:
        print("Virgo" if dia < 23 else "Libra")
    case 10:
        print("Libra" if dia < 23 else "Escorpio")
    case 11:
        print("Escorpio" if dia < 22 else "Sagitario")
    case 12:
        print("Sagitario" if dia < 22 else "Capricornio")