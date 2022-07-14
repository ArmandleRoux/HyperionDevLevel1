# Request input from user to privide fullname
fullname = input("Please enter your Fullname: \n")

# Calculate the lenght of the fullname with
# len() and print the appropriate response
if len(fullname) == 0:
    print("You haven’t entered anything. Please enter your full name.")
if len(fullname) < 4:
    print("""You have entered less than 4 characters.
Please make sure that you have entered your name and surname.""")
if len(fullname) > 25:
    print("""You have entered more than 25 characters.
Please make sure that you have only entered your full name.""")
if 4 < len(fullname) < 25:
    print("Thank you for entering your name.")
