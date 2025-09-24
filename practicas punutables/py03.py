print("area cuadradrado")
print("area rectangulo")
print("area triangulo")
print("area rombo")
print("area pentagono")
print("area hexagono")
print("area circulo")
print("area trapecio")
print("area paralelogramo")

figura = input("elige una figura: ")
area = 0
perimetro = 0

match figura:
    case "Cuadrado":
        lado = float(input("escribe el lado: "))
        area = lado * lado
        perimetro = 4 * lado
    case "Rectangulo":
        base = float(input("escribe la base:"))
        altura = float(input("escribe la altura:"))
        area = base * altura
    case "Triangulo":
        base = float(input("escribe la base:"))
        altura = float(input("escribe la altura:"))
        area = base * altura / 2
    case "Rombo":
        base = float(input("escribe la base:"))
        altura = float(input("escribe la altura:"))
        area = base * altura
    case "Pentagono":
        base = float(input("escribe la base:"))
        altura = float(input("escribe la altura:"))
        area = base * altura / 2 * 5
    case "Hexagono":
        lado = float(input("escribe el lado: "))
        perimetro = 6 * lado
        area = (3 * (3 ** 0.5) * lado * lado) / 2
