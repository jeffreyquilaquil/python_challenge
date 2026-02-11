def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def kilometers_to_miles(km):
    return km * 0.621371

def kilograms_to_pounds(kg):
    return kg * 2.20462

def main():
    print("--- Simple Unit Converter ---")
    print("1. Celsius to Fahrenheit")
    print("2. Kilometers to Miles")
    print("3. Kilograms to Pounds")
    
    try:
        choice = input("Select a conversion (1/2/3): ")
        value = float(input("Enter value to convert: "))
        
        if choice == '1':
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C is {result:.2f}°F")
        elif choice == '2':
            result = kilometers_to_miles(value)
            print(f"{value} km is {result:.2f} miles")
        elif choice == '3':
            result = kilograms_to_pounds(value)
            print(f"{value} kg is {result:.2f} lbs")
        else:
            print("Invalid choice!")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
