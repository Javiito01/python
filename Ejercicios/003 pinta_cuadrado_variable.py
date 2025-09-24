lado = int(input("Introduce el tamaño del lado del cuadrado: "))

for fila in range(lado):
    for columna in range(lado):
        print("*", end=" ")
    print()