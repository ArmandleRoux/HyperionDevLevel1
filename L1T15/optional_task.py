# Request input from user to provide a word and declare a new_string variable
# to the reversed value of user_string
user_string = input("Please enter a word: \n").lower()
new_string = user_string[::-1]

# If user_string is equal to the new_string the user_string is a palindrome
# Print result to console
if user_string == new_string:
    print("Your word is a palindrome!")
else:
    print("Your word is not a palindrome!")


