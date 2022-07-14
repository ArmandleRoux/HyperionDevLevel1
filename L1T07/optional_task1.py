# Request user input to provide an integer
num = int(input("Please type in a whole number: \n"))

# Calculate if integer provided is odd or even using modulus operator and print appropriate response to console
if num%2 == 0:
    print(f"{num} is an even number")
if num%2 == 1:
    print(f"{num} is an odd number")
