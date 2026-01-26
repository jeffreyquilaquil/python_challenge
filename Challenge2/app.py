
def calculator():
    operation = int(input("Operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n\nPlease select the operation: "))

    num1 = int(input("Please enter the first digit: "))
    num2 = int(input("Now enter the second number: "))

    try:
        match operation:
            case 1:
                result = num1 + num2
            case 2:
                result = num1 - num2
            case 3:
                result = num1 * num2
            case 4:
                result = num1 / num2
    except ValueError:
        print("Please select between the stated operations.") 

    print(f"The result is: {result}")

if __name__ == "__main__":
    calculator()