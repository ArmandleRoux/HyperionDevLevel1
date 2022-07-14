# Open file and assign it to a variable 'f' and declare a contents list to
# store information.
# Loop through every line redig the contents of each line to a list with all
# the content split. Print second value and initial of first value of each
# line to console. Close file after use.
f = open("DOB.txt", "r")
contents = [] 
print("Name:")
for line in f:
    contents = line.split(" ")
    print(f"{contents[0][0]} {contents[1]}")
f.close()

print("-"*80)

# Open file again and loop through lines and store values in contents list with
# all content split. Print the last 3 values in list which forms the Date of
# Birth. Close file after use.
f = open("DOB.txt", "r")
print("Date of Birth:")
for line in f:
    contents = line.split(" ")
    print(f"{contents[2]} {contents[3]} {contents[4][0:4]}")
f.close()
    

