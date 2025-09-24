print("calcular IMC")

peso = float(input("escribe tu peso en kg: "))
altura = float(input("escribe tu altura en metros: "))

imc = peso / (altura ** 2)

print(f"tu IMC es: {imc:.2f}")