# Request user to enter 3 numbers
num1 = int(input("Please enter a number: \n"))
num2 = int(input("Please enter another number: \n"))
num3 = int(input("Please enter a third and final number: \n"))
# Print the sum of the numbers to console
print(f"The sum of the numbers = {num1 + num2 + num3}")
# Print the result of num1 - num2 to console
print(f"First number - Second number = {num1 - num2}")
# Print the result of num 1 multiplied by num2
print(f"First number multiplied by third number = {num1 * num3}")
# Print the result of the sum of all numbers devided
# by the first number to console
print("Sum of all numbers devided by third number =" +
      f" {(num1 + num2 + num3)/num3}")


