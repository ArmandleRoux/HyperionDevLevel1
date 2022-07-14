#Request input from user to provide total number of students
total_students = int(input("How many student are registering? \n>"))

# Open file and ask students for ID numbers and write ID numbers to file
f = open("reg_form.txt", "w")
for i in range(0, total_students):
    f.write(input("Enter your ID number: \n")+ "\n")

# Close file after use
f.close()
