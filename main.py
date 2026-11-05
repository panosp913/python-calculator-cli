from calculator import add, subtract, multiply, divide

while True:
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Choose an option: ")
    try:
        if choice == "5":
            print("Goodbye!")
            break

        elif choice not in ("1", "2", "3", "4"):
            print("Invalid choice.")

        else:
            first_number = float(input("First number: "))
            second_number = float(input("Second number: "))

            if choice == "1":
                print(f"Result: {add(first_number, second_number)}")

            elif choice == "2":
                print(f"Result: {subtract(first_number, second_number)}")

            elif choice == "3":
                print(f"Result: {multiply(first_number, second_number)}")

            elif choice == "4":
                result = divide(first_number, second_number)
                if result is None:
                    print("Cannot divide by zero.")
                else:
                    print(f"Result: {result}")    

    except ValueError:            
            print("Invalid number.")
    