# Request input from user to provide a number
user_num = int(input("Enter a number to see it's timetable: \n"))
print("-"*80)

# Print the timetable of the number to the console
for i in range(1, 13):
    print(f"{user_num} x {i}\t= {user_num * i}")
