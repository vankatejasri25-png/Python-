# Python program to check if the number is an Armstrong number or not

#An Armstrong number is a number where the sum of its individual digits, each raised to the power of the total number of digits, equals the original number itself.eg: 153,1634, 9474

num = int(input("Enter a number: "))
n=len(str(num))

sum = 0

temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
