"""Command-line interface for the calculator."""

from calculator import add, subtract, multiply, divide


def main() -> None:
    operations = {
        "1": ("Addition", add),
        "2": ("Subtraction", subtract),
        "3": ("Multiplication", multiply),
        "4": ("Division", divide),
    }

    print("\n=== Python Calculator ===")
    for key, (name, _) in operations.items():
        print(f"{key}. {name}")
    print("q. Quit")

    while True:
        choice = input("\nChoose an operation (1-4 or q): ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Invalid choice. Please select 1, 2, 3, 4, or q.")
            continue

        try:
            first = float(input("Enter the first number: "))
            second = float(input("Enter the second number: "))
            name, operation = operations[choice]
            result = operation(first, second)
            print(f"{name} result: {result:g}")
        except ValueError as error:
            print(f"Input error: {error}")


if __name__ == "__main__":
    main()
