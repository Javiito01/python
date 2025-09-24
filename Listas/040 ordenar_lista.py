lista_numeros = [5, 2, 9, 1, 5, 6]

ascendente = []
descendente = []

while True:
    vacia = True
    for numero in lista_numeros:
        vacia = False
        break
    if vacia:
        break

    minimo = lista_numeros[0]
    for numero in lista_numeros:
        if numero < minimo:
            minimo = numero

    ascendente.append(minimo)

    nueva_lista = []
    eliminado = False
    for numero in lista_numeros:
        if numero == minimo and not eliminado:
            eliminado = True
        else:
            nueva_lista.append(numero)
    lista_numeros = nueva_lista

for numero in ascendente:
    descendente = [numero] + descendente

print("ascendente:", ascendente)
print("descendente:", descendente)
