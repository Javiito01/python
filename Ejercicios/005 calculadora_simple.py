print("calculadora simple")
num1 = float(input("introduce primer numero: "))
num2 = float(input("introduce el segundo numero: "))

print("elige una:")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion = input("elige una (1/2/3/4): ")

if opcion == "1":
    print(f"resultado: {num1 + num2}")
elif opcion == "2":
    print(f"resultado: {num1 - num2}")
elif opcion == "3":
    print(f"resultado: {num1 * num2}")
elif opcion == "4":
    if num2 != 0:
        print(f"resultado: {num1 / num2}")
    else:
        print("no se puede dividir por cero.")
else:
    print("opción no valida.")