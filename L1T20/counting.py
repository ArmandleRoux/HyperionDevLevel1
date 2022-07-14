# Declared a string to count it's characters and dictionary to use for 
# counting.
# Iterate through all the letters check first if key is already in
# dictionary if it is add 1 to it's value else set it's value to 1 
# Print result to console
sample_string = "google.com"

letters = {}

for char in sample_string:
    if char in letters:
        letters[char] += 1
    else:
        letters[char] = 1

print(letters)