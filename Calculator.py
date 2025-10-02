def calculator():
    print("Welcome to the Simple Calculator!")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        result = num1 + num2
        operation = '+'
    elif choice == '2':
        result = num1 - num2
        operation = '-'
    elif choice == '3':
        result = num1 * num2
        operation = '*'
    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
        operation = '/'
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
        return

    print(f"\nResult: {num1} {operation} {num2} = {result}")

# Run the calculator
calculator() 