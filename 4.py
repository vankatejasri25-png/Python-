d = int(input("Enter distance: "))
age = int(input("Enter age: "))
c = input("Enter class (A/B): ").upper()
fare = d * (3 if c == "A" else 2)
if age >= 60:
    fare *= 0.8
fare += 50
if input("Cancel ticket? (yes/no): ").lower() == "yes":
    fare += 100
print("Final Fare:", round(fare, 2))
