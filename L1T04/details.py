# Request input from user to provide their Name, Age, House Number and Street Name
name = input("Please enter your name: \n")
age = input("Please enter your age: \n")
house_number = input("Please enter your House Number: \n")
street_name = input("Please enter the name of your street: \n")
# Print to console a sentence containing all variables using .format()
print("This is {0} he is {1} years old and lives at house number {2} on {3}"
      .format(name, age, house_number, street_name))
