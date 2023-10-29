def temperature_converter():
    print("Welcome to the Temperature Converter!")
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = int(input("Enter your choice (1 or 2): "))
        if choice not in [1, 2]:
            raise ValueError("Invalid choice. Enter 1 or 2.")
        
        value = float(input("Enter the temperature value to convert: "))
        
        if choice == 1:
            result = (value * 9/5) + 32
            print(f"{value}°C is equal to {result}°F")
        else:
            result = (value - 32) * 5/9
            print(f"{value}°F is equal to {result}°C")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    temperature_converter()
