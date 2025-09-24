import random

num1 = int(input("escribe el primer numero: "))
num2 = int(input("escribe el segundo numero: "))
cantidad = int(input("cuantos numeros quieres: "))
for i in range(cantidad):
 print(random.randint(num1, num2))
