n=int(input("Enter the number of values:"))
sum=0
for i in range(1,n+1):
    num=float(input("Enter number" +str(i) + ":"))
    sum=sum+num
average=sum/n
print("Sum=",sum)
print("Average=",average)
