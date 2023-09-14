principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (as a decimal): "))
time = float(input("Enter time (in years): "))

simple_interest = principal * rate * time
print("Simple Interest:", simple_interest)

# Compound Interest
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (as a decimal): "))
time = float(input("Enter time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

amount = principal * (1 + (rate / n)) ** (n * time)
compound_interest = amount - principal
print("Compound Interest:", compound_interest)