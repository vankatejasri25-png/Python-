# program 6
num=int(input("enter num value:"))
original=sum
rev=0
while num>0:
     rem=num%10
     rev=rev*10+rem
     num=num//10
if original==sum:
      print("given number is palindrome")
else:
     print("given number is not palindrome ")
