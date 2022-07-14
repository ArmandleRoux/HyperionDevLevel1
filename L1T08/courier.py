# Request input from user to provide the price of their product and the distance of the delivery
product_price = float(input("What is the price of the package you would like to purchase? \n"))
distance = float(input("What is the total distance of delivery? (km) \n"))

# Request input from user to answer questions that will determine the parcel's final cost
cost_per_km = input("Would you like to use air or freight? Type air or freight \n").lower()
insurance_type = input("Would you like full insurance or limited? Type full or limited \n").lower()
gift = input("Is it a gift? Type yes or no \n")
delivery_type = input("Standard or priority deliviry? Type standard or priority \n")

# Use user input of questions to determine the final cost based on
# their provided preferences using if-else statements
if cost_per_km == "air":
    cost_per_km = 0.36
else:
    cost_per_km = 0.25

if insurance_type == "full":
    insurance_type = 50.00
else:
    insurance_type = 25.00

if gift == "yes":
    gift = 15.00
else:
    gift = 0

if delivery_type == "standard":
    delivery_type = 20.00
else:
    delivery_type = 100.00

# Calculate the final total_cost
total_cost = round(product_price + (distance * cost_per_km) + insurance_type + gift + delivery_type, 2)

 # Print total_cost to console
print(f"The total cost of your package is R{total_cost}.")
