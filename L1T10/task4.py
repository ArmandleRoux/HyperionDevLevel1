# Request input from user to provide a random integer
user_num = int(input("Please enter a random whole number: \n"))

# Check to see if user number is divisible by 2 , 5, both or neither and print
# the appropriate message to console
if user_num%2 == 0 and user_num%5 == 0:
    print(f"The number {user_num} is divisible by 2 and 5")
elif user_num%2 == 0 or user_num%5 == 0:
    print(f"The number {user_num} is divisible by 2 or 5")
else:
    print(f"The number {user_num} is not divisible by 2 or 5")

