# Request input from user to provide a name and capitalize the 
# first letter
name = input("Enter your name: ").capitalize()
names_list = []

# While name is not equal to "John" then append name to list and 
# ask for another name
while name != "John":
    names_list.append(name)
    name = input("Enter your name: ").capitalize()

# Print list of incorrect names
print(f"Incorrect names: {names_list}")
