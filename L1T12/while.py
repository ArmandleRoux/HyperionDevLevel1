# Request input from user to provide a number and declare variables
# for use in while loop
user_num = float(input("Please enter a number: \n"))
i = 0
num_total = 0

# Calculate total of numbers and count each number using a while loop to
# continue asking user for more input untill they enter '-1'
while user_num != -1:
    i +=1
    num_total += user_num
    user_num = float(input("Enter another number: " +
                         "(Type '-1' to calculate average)\n"))

# Calculate average of all numbers entered and print result to console
average = round(num_total/i, 2)
print("-"*80)
print(f"Average between all numbers entered: \t {average}")
print("-"*80)
    
