b = float(input("Basic salary: "))
a = float(input("Allowances: "))
o = float(input("Overtime: "))
i = float(input("Incentives: "))
g = b + a + o + i
d = g * 0.05 if g <= 20000 else g * 0.10
print("Gross:", g, "Deduction:", d, "Net Salary:", g-d)
