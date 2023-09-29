numbers = [] 
for i in range (10):
     try:
         num= int (input("Enter integer"))
         numbers.append(num)
     except ValueError:
        print(" Invalid input")

print("combinations of picking 2 numbers:")
for i in range (10):
    for j in range (i+1, 10):
        print ( numbers [i]," and ", numbers [j])