# Defined function to add numbers
def add_num(num1, num2):
    print(f"{num1} + {num2}")
    print(f"Answer = {num1+num2}")

# Defined function to subtract numbers
def subtract_num(num1, num2):
    print(f"{num1} - {num2}")
    print(f"Answer = {num1-num2}")

# Defined function to multiply numbers
def multiply_num(num1, num2):
    print(f"{num1} x {num2}")
    print(f"Answer = {num1*num2}")

# Defined function to divide numbers
def divide_num(num1, num2):
    print(f"{num1} / {num2}")
    print(f"Answer = {round(num1 / num2, 2)}")

# Request input from user to provide 2 numbers and a choice for what
# to do with those numbers.
num1 = int(input("Please enter a number: \n>"))
num2 = int(input("Please enter another number: \n>"))

choice = int(input("What would you like to do with these numbers?"
               "(Choose a number)\n"
               "1 - Add \n"
               "2 - Subtract \n"
               "3 - Multiply \n"
               "4 - Divide \n>"))
print("-"*80)

# Check user choice and calculate result accordingly
if choice == 1: answer = add_num(num1, num2)
elif choice == 2: answer = subtract_num(num1, num2)
elif choice == 3: answer = multiply_num(num1, num2)
elif choice == 4:  answer = divide_num(num1, num2)
