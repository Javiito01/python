secreto = 7 
intentos = 0

while intentos < 6:
    numero = int(input("adivina el numero: "))
    if numero == secreto:
        print("bien")
        break
    intentos += 1

if numero != secreto:
    print("casi campeon,el numero era 7.")