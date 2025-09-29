lista = [1,2,3,4,5,6,7,8,9]
valormaximo = lista[0]

for i in range(len(lista)):
  if lista[i] > valormaximo:
        valormaximo = lista[i]

print("El valor maxmio de la lista es:",valormaximo)
        