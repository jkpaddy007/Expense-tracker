def load_expenses():
expenses = []

try:
    with open("expenses.txt", "r") as file:
        for line in file:
            description, category, amount = line.strip().split("|")

            expense = {
                "description": description,
                "category": category,
                "amount": float(amount)
            }

            expenses.append(expense)

except FileNotFoundError:
    pass

return expenses

def save_expenses(expenses):
with open("expenses.txt", "w") as file:
for expense in expenses:
file.write(
f"{expense['description']}|"
f"{expense['category']}|"
f"{expense['amount']}\n"
)

def add_expense(expenses):
description = input("Enter expense description: ")
category = input("Enter category: ")

try:
    amount = float(input("Enter amount: "))

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

except ValueError:
    print("Please enter a valid number.")
    return

expense = {
    "description": description,
    "category": category,
    "amount": amount
}

expenses.append(expense)
save_expenses(expenses)

print("Expense added successfully!")

def view_expenses(expenses):
if not expenses:
print("No expenses recorded.")
return

for number, expense in enumerate(expenses, start=1):
    print(
        f"{number}. {expense['description']} | "
        f"{expense['category']} | "
        f"Rs. {expense['amount']:.2f}"
    )

def show_total(expenses):
total = sum(expense["amount"] for expense in expenses)
print(f"Total expenses: Rs. {total:.2f}")

def main():
expenses = load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        show_total(expenses)

    elif choice == "4":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")

if name == "main":
main()
