import math

operator = input("Click operation +, -, *, /, **, sin, cos, tan (Click 0 to finish): ")
while True:
    if operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "**":
        num_1 = int(input("Enter the first number: "))
        num_2 = int(input("Enter the second number: "))
        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        elif operator == "**":
            result = num_1 ** num_2
        elif operator == "/":
            if num_2 == 0:
                print("It is impossible to divide by zero")
            else:
                result = num_1 / num_2
    elif operator == "sin" or operator == "cos" or operator == "tan":
        num_1 = int(input("Enter the number: "))
        if operator == "sin":
            result = math.sin(num_1)
        elif operator == "cos":
            result = math.cos(num_1)
        elif operator == "tan":
            result = math.tan(num_1)
    if operator == "0":
        break
    print("Result: ", result, "\n")
    operator = input("Click operation +, -, *, /, **, sin, cos, tan (Click 0 to finish): ")
