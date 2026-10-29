p = float(input("Enter product price: "))
q = int(input("Enter quantity: "))
total = p * q
discount = min(total * 0.10, 200) if total >= 1000 else 0
bill = (total - discount) * 1.05
print("Total Bill:", round(bill, 2))
