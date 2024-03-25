income = 0
expenses = []
categories = []
amounts = []

# Function to input income
def input_income():
    global income
    income = float(input("Enter your income: "))

# Function to input expenses
def input_expenses():
    category = input("Enter the expense category: ")
    amount = float(input("Enter the expense amount: "))
    expenses.append((category, amount))
    categories.append(category)
    amounts.append(amount)

# Function to calculate remaining budget
def calculate_budget():
    total_expenses = sum(amounts)
    remaining_budget = income - total_expenses
    return remaining_budget

# Function to analyze expenses
def analyze_expenses():
    expense_analysis = {}
    for category in categories:
        expense_analysis[category] = expenses.count(category)
    return expense_analysis

# Function to store transactions in a file
def store_transactions():
    with open("transactions.txt", "w") as file:
        for category, amount in expenses:
            file.write(f"{category}: {amount}\n")

# Main function
def main():
    input_income()
    while True:
        choice = input("Enter '1' to input expenses, '2' to calculate remaining budget, '3' to analyze expenses, or '4' to exit: ")
        if choice == '1':
            input_expenses()
        elif choice == '2':
            remaining_budget = calculate_budget()
            print(f"Remaining budget: {remaining_budget}")
        elif choice == '3':
            expense_analysis = analyze_expenses()
            print("Expense analysis:")
            for category, count in expense_analysis.items():
                print(f"{category}: {count}")
        elif choice == '4':
            store_transactions()
            print("Transactions stored in 'transactions.txt'")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
main()