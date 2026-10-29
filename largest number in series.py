# Ask the user for the total number of elements
n = int(input("Enter the number of elements: "))

# Initialize the first number as the largest
largest = float(input("Enter number 1: "))

# Loop to get the remaining numbers
for i in range(2, n + 1):
    num = float(input(f"Enter number {i}: "))
    # Update largest if the current number is greater
    if num > largest:
        largest = num

print(f"The largest number is: {largest}")
