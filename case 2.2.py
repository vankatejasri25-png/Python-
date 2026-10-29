u = int(input("Enter units: "))
p = float(input("Enter previous bill: "))
b = u*2 if u <= 100 else 200+(u-100)*3 if u <= 200 else 500+(u-200)*5
b += 50 + (b+50)*0.05 - (50 if b+50 > 1000 else 0)
print("Bill:", round(b, 2), "Unusual Increase" if b > 1.5*p else "Normal Bill")