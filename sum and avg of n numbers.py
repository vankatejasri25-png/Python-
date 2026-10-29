n = int(input("How many numbers do you want to enter? "))
numbers = []

for i in range(1,n+1):
    num = float(input(f"Enter number {i}: "))
    numbers.append(num)

# Calculate sum and average
total_sum = sum(numbers)
if n>0:
    average = total_sum / n
else:
    print("0")

print(f"\nSum of {n} numbers: {total_sum}")
print(f"Average of {n} numbers: {average}")
