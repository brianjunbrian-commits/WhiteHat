while True:
    operator = input("Enter operator (+, -, *, /, q): ")

    if operator == "q":
        print("Calculator closed")
        break

    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter Second number: "))

    def add_numbers(number1, number2):
        result = number1 + number2
        return result

    def subtract_numbers(number1, number2):
        result = number1 - number2
        return result

    def multiply_numbers(number1, number2):
        result = number1 * number2
        return result

    def divide_numbers(number1, number2):
        if number2 == 0:
            return "Cannot divide by zero"
        else: 
            result = number1 / number2 
            return result

    if operator == "+":
        answer = add_numbers(first_number, second_number)
    elif operator == "-":
        answer = subtract_numbers(first_number, second_number)
    elif operator == "*":
        answer = multiply_numbers(first_number, second_number)
    elif operator == "/":
        answer = divide_numbers(first_number, second_number)
    else:
        answer = "Invalid operator"

    print("Result:", answer)

# Need to fix some codes