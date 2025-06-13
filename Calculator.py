def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        try:
            choice = input("Enter your choice (1/2/3/4): ")
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
          

            if choice == '1':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                if num2 != 0:
                    result = num1 / num2
                    print(f"{num1} / {num2} = {result}")
                else:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid choice. Please choose a valid option.")

            cont = input("Do you want to continue? (y/n): ")
            if cont.lower() != 'y':
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    calculator()