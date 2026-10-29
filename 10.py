amount = float(input("Enter foreign expense: "))
rate = float(input("Enter exchange rate: "))
fee = float(input("Enter conversion fee: "))
budget = float(input("Enter budget: "))
total = amount * rate + fee
print("Total Expense:", total)
print("Within Budget" if total <= budget else "Over Budget")
