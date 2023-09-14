import math

# Input coefficients a, b, and c from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Calculate the discriminant (the value inside the square root)
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Two distinct real roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)
elif discriminant == 0:
    # One real root (repeated)
    root = -b / (2*a)
    print("One real root:")
    print("Root:", root)
else:
    # No real roots (complex roots)
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("Complex roots:")
    print("Root 1:", real_part, "+", imaginary_part, "i")
    print("Root 2:", real_part, "-", imaginary_part, "i")