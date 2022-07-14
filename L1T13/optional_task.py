# Request input from user to provide a number
num = int(input("Please enter a number: \n"))

print("-"*80)

# Print out the number to console as many times as it's value if number is
# greater tahn 10 else print error message
if num > 10:
    for i in range(0,num):
        print(num)
else:
    print("Sorry, too small.")
