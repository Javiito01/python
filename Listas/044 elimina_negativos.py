lista = [1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
i = 0
while i < len(lista):
    if lista[i] < 0:
        lista.remove(lista[i])
    else:
        i += 1
print("elementos negativos fuera:", lista)