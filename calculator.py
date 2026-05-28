def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
while True:
    choose = input("Choose an Operation"
                   "\n1. Addition"
                   "\n2. Subtraction"
                   "\n3. Multiplication"
                   "\n4. Division"
                   "\n5. Exit"
                   "\nEnter your choice (1-5): ")
    if choose == '5':
        print("Very Good! Brat/Bitch, use your fucking brain.")
        break
    if choose not in ['1', '2', '3', '4']:
        print("Brat/Bitch, do you even know how to read? Try again.")
        continue
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numbers.")
        continue
    except TypeError:
        print("Error: Invalid input. Please enter numbers.")
        continue
    conformation = input("Are you sure you want to perform this operation? (y/n): ")
    if conformation.lower() == "y":
        if choose == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choose == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choose == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choose == '4':
            result = divide(num1, num2)
            print("Result:", result)
        operators = {'1':'+', '2':'-', '3':'*', '4':'/'}
        entry = f"{num1} {operators[choose]} {num2} = {result}\n"
    else:
        print("Operation cancelled.")
        entry = "Operation cancelled.\n"
    try:
        with open("history.txt", "r") as f:
            history = f.readlines()
    except FileNotFoundError:
        history = []
    history.append(entry)
    history = history[-7:]
    with open("history.txt", "w") as f:
        f.writelines(history)
    show_history = input("Do you want to see the history of calculations? (y/n): ")
    if show_history.lower() == "y":
        with open("history.txt", "r") as f:
            print(f.read())
    else:
        print("Request denied.")
    again = input("Do you want to perform another operation? (y/n): ")
    if again.lower() == "n":
        print("Very Good! Brat/Bitch, use your fucking brain.")
        break