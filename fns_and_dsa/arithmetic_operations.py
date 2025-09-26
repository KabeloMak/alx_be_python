def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
    if operation == "add":
        print("Result: ", num1 + num2)
    if operation == "subtract":
        print("Result: ", num1 - num2)
    if operation == "multiply":
        print("Result: ", num1/num2)
    if operation == "divide":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result: ", num1/num2)

perform_operation()