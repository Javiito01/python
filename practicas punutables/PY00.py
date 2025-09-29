palabra = input("Escribe una palabra:")
vocales = "aeiou"
contador = 0
for i in palabra:
    if i.lower() in vocales:
        contador +=  1
        
print(palabra,"tiene", contador, "vocales")