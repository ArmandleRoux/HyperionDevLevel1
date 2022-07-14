# Request input from user to enter their favourite restaurant and number
fav_rest = input("Please enter your favorite restaurant: \n")
int_fav = int(input("Please enter your favourite number: \n"))
# Print variables to console on seperate lines
print(fav_rest)
print(int_fav)
# This code will produce an error because the string variable contains letters or other characters that do not
# qualify as integers and cannot be casted to integers thus producing an error
int(fav_rest)
