# Declare original string and string to store new value
test_string = "Hello World"
new_string = ""

# Iterate through the string and change each alternate character to uppercase
# and each other alternate character to lowercase
# Print result to console
for i in range(0 , len(test_string)):
  if i%2 == 0:
    new_string += test_string[i].upper()
  else:
    new_string += test_string[i].lower()
       
print(new_string)
