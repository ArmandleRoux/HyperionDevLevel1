# Request input from user to provide a number less than or equal to 100
user_num = int(input("Please enter a number less than or equal to 100: \n>"))

# Evaluate user answer and determine if answer is valid
while user_num > 100:
    user_num = int(input("Your number is greater than 100 please enter a"+
                         " smaller number! \n>"))

# Calculate if user_num is even or odd and print appropriate result
if user_num%2 == 0:
    print(user_num * 2)
else:
    print(user_num * 3)
