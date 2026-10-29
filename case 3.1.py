c = float(input("Consultation charge: "))
d = float(input("Diagnostic charge: "))
t = float(input("Treatment charge: "))
b = c + d + t
if b > 5000: b *= 0.90
print("Final Bill:", b)
print("Category:", "Low" if b <= 3000 else "Medium" if b <= 7000 else "High")
