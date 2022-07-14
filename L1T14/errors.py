# This example program is meant to demonstrate errors.
 
# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.


print("Welcome to the error program") # syntax error
print("\n") # syntax error

ageStr = "24" #I'm 24 years old.       syntax and runtime error
age = int(ageStr)                    # syntax error
print("I'm "+f"{age}"+" years old.") # syntax error
three = 3                            # syntax and runtime error

answerYears = age + three            # syntax and runtime error

# syntax and logic error
print ("The total number of years: " + f"{answerYears}")
answerMonths = (answerYears*12) +6        # runtime and logic error
# syntax and runtime error
print ("In 3 years and 6 months, I'll be " + f"{answerMonths}" + " months old")

#HINT, 330 months is the correct answer

