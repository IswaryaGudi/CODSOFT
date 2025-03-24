def simple_calculator(): 
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("You have entered invalid input. Please enter numbers.")
        return
    operation = input("Enter the operation (+, -, *, /): ")
    if operation == '+':
        result = num1 + num2
        print("Addition of 2 numbers is: \n"f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print("Subtraction of 2 numbers is: "f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print("Multiplication of 2 numbers is: "f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Division of 2 numbers is: "f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation.")

simple_calculator()
