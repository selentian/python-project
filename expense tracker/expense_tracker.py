import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Data storage
expenses = {}  # {date: {category: amount in INR}}
categories = ["Food", "Transport", "Entertainment", "Other"]

# Currency symbol
CURRENCY = "₹"

# Log daily expense
def log_expense(date, category, amount):
    if date not in expenses:
        expenses[date] = {}
    expenses[date][category] = expenses[date].get(category, 0) + amount

# Generate summary (weekly or monthly)
def generate_summary(period="weekly"):
    today = datetime.now()
    if period == "weekly":
        start_date = today - timedelta(days=7)
    else:  # monthly
        start_date = today.replace(day=1) - timedelta(days=30)
    
    total = 0
    summary = {}
    for date in sorted(expenses.keys()):
        if date >= start_date:
            for cat, amt in expenses[date].items():
                summary[cat] = summary.get(cat, 0) + amt
                total += amt
    
    print(f"\n{period.capitalize()} Summary (from {start_date.date()} to {today.date()}):")
    for cat, amt in summary.items():
        print(f"{cat}: {CURRENCY}{amt:.2f}")
    print(f"Total Spending: {CURRENCY}{total:.2f}")
    return summary

# Visualize spending
def visualize_spending(summary):
    categories = list(summary.keys())
    amounts = list(summary.values())
    plt.bar(categories, amounts, color='lightcoral')
    plt.title("Spending Breakdown (INR)")
    plt.xlabel("Categories")
    plt.ylabel(f"Amount ({CURRENCY})")
    plt.show()

# Main Program
if __name__ == "__main__":
    print("Expense Tracker with Data Analysis (INR)")
    
    # Interactive input loop
    while True:
        print("\nAvailable categories:", ", ".join(categories))
        cat = input("Enter category (or 'quit' to exit): ")
        if cat.lower() == 'quit':
            break
        if cat in categories:
            try:
                amount = float(input(f"Enter amount in {CURRENCY}: "))
                if amount < 0:
                    print("Amount cannot be negative!")
                    continue
                log_expense(datetime.now(), cat, amount)
                print("Expense logged!")
            except ValueError:
                print("Please enter a valid number!")
        else:
            print("Invalid category. Use:", ", ".join(categories))
    
    # Generate summaries and visualize if there are expenses
    if expenses:
        weekly_summary = generate_summary("weekly")
        monthly_summary = generate_summary("monthly")
        visualize_spending(weekly_summary)
    else:
        print("No expenses logged yet!")