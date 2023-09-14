import math

# Input the height and angle (in degrees) from the user
height = float(input("Enter the height to be reached (in meters): "))
angle_degrees = float(input("Enter the angle of the ladder (in degrees): "))

# Convert the angle from degrees to radians
angle_radians = math.radians(angle_degrees)

# Calculate the length of the ladder using trigonometry (Pythagoras' theorem)
ladder_length = height / math.sin(angle_radians)

# Print the length of the ladder needed
print(f"The length of the ladder needed is {ladder_length:.2f} meters.")