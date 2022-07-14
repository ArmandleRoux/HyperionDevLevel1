# Declared 3 int variables and assign them values
num1 = 25
num2 = 30
num3 = 35

# Check to see which number is bigger
# between num1 and num2 then print that number to console
if num1 > num2:
    print(num1)
else:
    print(num2)

# Check to see if num1 was an even or odd number and print result to console
if num1%2 == 0:
    print(f"{num1} is an even value")
else:
    print(f"{num1} is a odd value")

# Check all 3 number with a conditional statement to
# determine their order from largest to smallest and print result to console
if num1 < num2 and num1 < num3 and num2 < num3:
    print(f"{num3}, {num2}, {num1}")
elif num1 < num2 and num1 < num3 and num3 < num2:
    print(f"{num2}, {num3}, {num1}")
elif num2 < num1 and num2 < num3 and num1 < num3:
    print(f"{num3}, {num1}, {num2}")
elif num2 < num1 and num2 < num3 and num3 < num1:
    print(f"{num1}, {num3}, {num2}")
elif num3 < num1 and num3 < num2 and num1 < num2:
    print(f"{num2}, {num1}, {num3}")
else:
    print(f"{num1}, {num2}, {num3}")


    
