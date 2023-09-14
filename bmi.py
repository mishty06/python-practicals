weight=float(input("Enter your weight : "))
height=float(input("Enter your height : "))
bmi= weight/ height**2
if bmi>19 and bmi<25:
    print("You are HEALTHY",bmi)
elif bmi>25:
    print("You are OVERWEIGHT ",bmi)
else:
    print("You are UNDERWEIGHT",bmi)