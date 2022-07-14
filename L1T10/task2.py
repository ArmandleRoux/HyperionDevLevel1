# Import math module for use of PI
import math

#Request user input to provide the shape of the building to determine
# area properties
building_shape = input("Please enter the shape of the building: " +
                       "\n(square, rectangular or round) \n").lower()

# Check to see what shape was entered and request input from user to
# provide neccessary measurements. Once input is received calculate
# area with measurements and print result to console
if building_shape == "square":
    length = float(input("Please enter the length of the square: \n"))
    area = round(length**2, 2)
    print(f"The area of the building is {area}")
elif building_shape == "round":
    radius = float(input("Please enter the radius: \n"))
    area = round(math.pi * radius**2, 2)
    print(f"The area of the building is {area}")
else:
    length = float(input("Please enter the length: \n"))
    width = float(input("Please enter the width: \n"))
    area = round(length * width ,2)
    print(f"The area of the building is {area}")
