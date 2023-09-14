no_hours=int(input("Ebter number of hours you worked : "))
rate=float(input("Enter your hourly rate : "))
if no_hours>=40:
    rate=rate+1

total_wages=no_hours*rate
print("Total wages: ",total_wages)
