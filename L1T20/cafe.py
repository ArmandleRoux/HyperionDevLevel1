# Declred list for menu and 2 dictionaries for price 
# and quantity of stock respectively.
# With a for loop iterate through both dictionaties by
# iterating through the list.
# Using data in dictionaries calculate the stock worth
# in the cafe of each individual item aswell as the total
menu = ["Pizza", "Burgers", "Ribs", "Chips"]

stock = {"Pizza": 10,
         "Burgers": 20,
         "Ribs": 7,
         "Chips":25}

price = {"Pizza" : 30.50,
         "Burgers": 25.90,
         "Ribs": 35.00,
         "Chips": 10.00}

total_stock_worth = 0

print("-"*80)
print("Total stock worth of each item: ")
print("-"*80 + "\n")
for item in menu:
    total_stock_worth += round(stock[item] * price[item], 2)
    item_stock_worth = round(stock[item] * price[item], 2)
    print(f"{item}      \tR{item_stock_worth}")
    
print(f"\nTotal stock:   \tR{total_stock_worth}")
    