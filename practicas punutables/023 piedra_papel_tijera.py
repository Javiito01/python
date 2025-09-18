jugador1 = input("1, elige: piedra, papel o tijera: ")
jugador2 = input("2, elige: piedra, papel o tijera: ")

match (jugador1, jugador2):
    case (a, b) if a == b:
        print("empate")
    case ("piedra", "tijera") | ("papel", "piedra") | ("tijera", "papel"):
        print("gana el 1")
    case ("tijera", "piedra") | ("piedra", "papel") | ("papel", "tijera"):
        print("gana el 2")