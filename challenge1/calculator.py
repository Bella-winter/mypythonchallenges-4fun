
#simple calculator
# Ask the user to enter two numbers
x = float(input("Enter x: "))
y = int(input("Enter y: "))

# Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the calculation and print the result
if operation == "+":
    result = x + y
    print(f"The result of {x} + {y} is {result}")
elif operation == "-":
    result = x - y
    print(f"The result of {x} - {y} is {result}")
elif operation == "*":
    result = x * y
    print(f"The result of {x} * {y} is {result}")
elif operation == "/":
    result = x / y
    print(f"The result of {x} / {y} is {result}")
else: 
    print("Invalid operation. Please choose from '+', '-', '*', '/'.")
