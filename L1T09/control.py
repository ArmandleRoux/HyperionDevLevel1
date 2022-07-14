# Request input from user to provide their age
age = int(input("Please enter your age: \n"))

# Check if age is over 18, between 16 and 18 or under 18
# and print appropriate response to console
if age >= 18:
    print("You are old enough!")
elif 16 < age < 18:
    print("Almost there!")
else:
    print("You're just too young!")

