numero = int(input("escribe un numero: "))
a = 0
b = 1
for i in range (numero - 1):
    print(a, end=" ")
    a, b = b, a + b
print(a)