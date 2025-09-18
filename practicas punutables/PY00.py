palabra = input("Escribe una palabra:")
vocales = 0
for letra in palabra:
    if letra.lower() in "aeiou":
        vocales +=  1
        print(vocales)
        print("La palabra tiene vocales")