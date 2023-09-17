cost = float(input("Enter the cost in dollars: "))
payment = float(input("Enter the payment in dollars: "))

# Calculate the change in dollars and cents
change = payment - cost
change_cents = int(change * 100)

# Calculate the number of quarters, dimes, nickels, and pennies
quarters = change_cents // 25
change_cents %= 25

dimes = change_cents // 10
change_cents %= 10

nickels = change_cents // 5
change_cents %= 5

pennies = change_cents

# Print the change breakdown
print("Change in quarters:", quarters)
print("Change in dimes:", dimes)
print("Change in nickels:", nickels)
print("Change in pennies:", pennies)