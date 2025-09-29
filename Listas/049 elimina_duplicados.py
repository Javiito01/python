listaoriginal = [1, 2, 2, 3, 4, 4, 5, 1]
listasinduplicados = []

for i in listaoriginal:
    if i not in listasinduplicados:
        listasinduplicados.append(i)

print(listasinduplicados)