def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    current_salary = get_valid_float("Enter current salary: ")
    adjustment_percentage = get_valid_float("Enter adjustment percentage (0-100): ")

    if adjustment_percentage < 0:
        raise ValueError("Adjustment percentage cannot be negative.")

    if adjustment_percentage > 100:
        print("Warning: Percentage is unusually high.")

    new_salary = current_salary * (1 + adjustment_percentage / 100)

    print(f"New Salary: ${new_salary:.2f}")

main()