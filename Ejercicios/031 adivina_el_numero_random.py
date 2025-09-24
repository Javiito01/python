import random

num1 = random.randint(1, 10)
print("adivina entre 1 y 10")

while True:
    intento = int(input("escribe un numero: "))
    if intento == num1:
        print("bueena.")
        break
    elif intento < num1:
        print("demasiado bajo")
    else:
        print("demasiado alto")
