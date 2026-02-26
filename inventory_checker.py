def get_valid_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def check_inventory(inventory, threshold):

    try:
        percentage = (inventory / threshold) * 100

        if inventory < threshold:
            print("Reorder Alert: Inventory below threshold!")
        else:
            print("Inventory level is sufficient.")

        print(f"Inventory is {percentage:.2f}% of threshold.")

    except ZeroDivisionError:
        print("Threshold cannot be zero. Please enter a non-zero value.")
        return False  # Signal failure so main can retry

    return True  


def main():
    while True:
        inventory = get_valid_integer("Enter current inventory level: ")
        threshold = get_valid_integer("Enter minimum reorder threshold: ")

        success = check_inventory(inventory, threshold)

        if success:
            break  # Exit loop only if calculation succeeds



main()