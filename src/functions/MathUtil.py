import math


def CallMath():
    num1 = input("Укажите первое значение: ")
    num2 = input("Укажите второе значение: ")
    why = input("Укажите действие (+, -, *, /)")
    
    if why == "+":
        print("Ответ:", int(num1) + int(num2))
        
    elif why == "-":
        print("Ответ:", int(num1) - int(num2))

    elif why == "*":
        print("Ответ:", int(num1) * int(num2))

    elif why == "/":
        print("Ответ:", int(num1) // int(num2))

    else:
        print("Неизвестное действие:")