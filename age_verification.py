def get_customer_age():
    while True:
        try:
            age = int(input("Enter customer's age: "))

            if age <= 0:
                print("Age must be a positive number.")
            else:
                return age

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

        except NameError:
            print("A variable was referenced incorrectly.")


def main():
    customer_age = get_customer_age()

    if customer_age >= 18:
        print("Customer is eligible for the promotion.")
    else:
        print("Customer is NOT eligible for the promotion.")

main()