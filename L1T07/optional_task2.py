# Request input from user to provide yes/no answers for the 3 questions
temp_bool = input("Is it warmer than 20 degrees?(yes/no) \n")
day_bool = input("Is it currently a weekday?(yes/no) \n")
sunny_bool = input("Is it sunny outside?(yes/no) \n")

# Declare variables to store outfit in
shirt = ""
pants = ""
accessory = ""

# Change yes/no answers to boolean True/Flase
if temp_bool.lower() == "yes":
    temp_bool = True
else:
    temp_bool = False

if day_bool.lower() == "yes":
    day_bool = True
else:
    day_bool = False

if sunny_bool.lower() == "yes":
    sunny_bool = True
else:
    sunny_bool = False

# Check boolean value and set outfit variables accordingly
if temp_bool:
    shirt = "short-sleeved shirt"
else:
    shirt = "long-sleeved shirt"

if day_bool:
    pants = "jeans"
else:
    pants = "shorts"

if sunny_bool:
    accessory = "cap"
else:
    accessory = "raincoat"

# Print to console the final put together outfit
print(f"The temperature suggests that you wear a {shirt} with {pants}. A {accessory} can also come in handy.")
