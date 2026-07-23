a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("What operation? (+, -, *, /): ")
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b != 0:
        result = a / b
    else:
        result = "Error: Division by zero"

print(result)
