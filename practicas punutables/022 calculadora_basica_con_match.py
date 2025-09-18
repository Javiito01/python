num1 = int(input("dime el primer numero: "))
num2 = int(input("dime el segundo numero: "))
operacion = input("elige operación +, -, *, /: ")

match operacion:
    case "+":
        resultado = num1 + num2
        print("resultado:", resultado)
    case "-":
        resultado = num1 - num2
        print("resultado:", resultado)
    case "*":
        resultado = num1 * num2
        print("resultado:", resultado)
    case "/":
        if num1 > num2 and num2 != 0:
            resultado = num1 / num2
            print("resultado:", resultado)
        elif num2 == 0:
            print("no se puede dividir por cero.")
        else:
            print("el dividendo debe ser mayor que el divisor.")