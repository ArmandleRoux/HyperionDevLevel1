# Request input from user to provide student names
student_name = input("Enter the name of a student:"+
                     "(Type 'stop'to end) \n").lower()
number_of_students = 0

# Calculate amount of student entered using while loop and student_name
# as control variable. Keep asking for names untill user types 'stop'
while student_name != "stop":
    number_of_students += 1
    student_name = input("Enter another name:(Type 'Stop' to end) \n").lower()                   

# Print final result to console
print("-"*80)
print(f"Total number of students entered: \t{number_of_students}")
print("-"*80)
