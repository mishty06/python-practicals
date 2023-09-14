print("Enter point A in (x1,y1) format")
x1=int(input("Enter x1"))
y1=int(input("Enter y1"))
print("Enter point B in (x2,y2) format")
x2=int(input("Enter x2"))
y2=int(input("Enter y2"))
numerator= y2-y1
denominator=x2-x1

slope=numerator / denominator
print("Slope of the given points is : ", slope)