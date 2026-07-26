while True:
    operator = input("Enter operator (+, -, *, /, q): ")

    if operator == "q":
        print("Calculator closed")
        break

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))

    if operator == "+":
        result = first_number + second_number
        print("Result:", result)

    elif operator == "-":
        result = first_number - second_number
        print("Result:", result)

    elif operator == "*":
        result = first_number * second_number
        print("Result:", result)

    elif operator == "/":
        if second_number == 0:
            print("Division by zero")
        else:
            result = first_number / second_number
            print("Result:", result)
        
    else:
         print("Invalid operator")