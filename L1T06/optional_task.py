# import math module for use of sqrt()
import math

# Request input form user to provide the lengths of the 3 sides of a triagle
print("Enter the length of the sides of the triagle.")
side1 = float(input("Please provide the length of the first side: \n"))
side2 = float(input("Please provide the length of the second side: \n"))
side3 = float(input("Please provide the length of the third side: \n"))
# Calculate the area of th triagle
s = (side1 + side2 + side3)/2
area = round(math.sqrt(s * (s-side1) * (s-side2) * (s-side3)), 2)
# Print the result of the area to console
print(f"The area of the triagle = {area}")
