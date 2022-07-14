# Declared dictionary with abbreviations.
# Add 2 more abbreviations to dictionary
# Request inputfrom user ot provide an abbreviation. Check if abbreviation
# is in dictionary and print to console the meaning
abrev_dict = {"API": "Application Programming Interface",
              "IDE": "Itegrated Development Environment",
              "SDK": "Software Development Toolkit",
              "UI" : "User Interface"}

abrev_dict["OOP"] = "Object-Oriented Programming"
abrev_dict["SSH"] = "Secure Shell"

user_abrev = input("Type in an abbreviation you would like to know: \n>").upper()

if user_abrev in abrev_dict:
    print(abrev_dict[user_abrev])
else:
    print("Abbreviation not found!")
