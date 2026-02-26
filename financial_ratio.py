def get_financial_input():
    profit = float(input("Enter total profit: "))
    revenue = float(input("Enter total revenue: "))
    return profit, revenue


def calculate_profit_margin(profit, revenue):
    return profit / revenue


def main():
    while True:
        try:
            profit, revenue = get_financial_input()
            ratio = calculate_profit_margin(profit, revenue)

        except ValueError:
        
            pass

        except ZeroDivisionError:
            print("Revenue cannot be zero. Please try again.")

        else:
            print(f"Profit Margin: {ratio * 100:.2f}%")
            break  


main()