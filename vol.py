import math

# Input radius from the user
radius = float(input("Enter the radius of the sphere: "))

# Calculate the area of the sphere
area = 4 * math.pi * (radius ** 2)

# Calculate the volume of the sphere
volume = (4/3) * math.pi * (radius ** 3)
print(" Area is : ",area)
print("Volume is : ",volume)