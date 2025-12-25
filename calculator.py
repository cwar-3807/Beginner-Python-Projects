# Creating an advanced calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2) # Addition
elif op == "-":
    print(num1 - num2) # Subtraction
elif op == "*":
    print(num1 * num2) # Multiplication
elif op == "/":
    print(num1 / num2) # Division
elif op == "//":
    print(num1 // num2) # Floor Division
elif op == "%":
    print(num1 % num2) # Modulus
elif op == "**":
    print(num1 ** num2) # Exponentiation
elif op == "log":
    print(log(num1, num2) if num1 > 0 and num2 > 0 and num2 != 1 else "Invalid logarithm") # Logarithms
elif op == ">":
    print(f"{num1} is greater than {num2}" if num1 > num2 else f"{num1} is NOT greater than {num2}") # Test greater than
elif op == "<":
    print(f"{num1} is less than {num2}" if num1 < num2 else f"{num1} is NOT less than {num2}") # Test less than
elif op == "=":
    print(f"{num1} is equal to {num2}" if num1 == num2 else f"{num1} is NOT equal to {num2}") # Test equality
elif op == "sin"
    print(sin(num1 / num2) if num1 <= num2 else "Invalid sine") # sine operator (num1 = opposite, num2 = hypotenuse)
elif op == "cos"
    print(cos(num1 / num2) if num1 <= num2 else "Invalid cosine") # cosine opeartor (num1 = adjacent, num2 = hypotenuse)
elif op == "tan":
    print(tan(num1 / num2)) # tangent operator (num1 = opposite, num2 = adjacent)
elif op == "cosec"
    print(cosec(num1 / num2) if num1 >= num2 else "Invalid cosecant") # cosecant operator (num1 = hypotenuse, num2 = opposite)
elif op == "sec"
    print(sec(num1 / num2) if num1 >= num2 else "Invalid secant") # secant operator (num1 = hypotenuse, num2 = adjacent)
elif op == "cot":
    print(cot(num1 / num2)) # cotangent operator (num1 = adjacent, num2 = opposite)
else:
    print("Invalid operator")
