n=int(input("enter the n value:"))
for num in range(1,n):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                break
        else:
           print(num,end=" ")
            
