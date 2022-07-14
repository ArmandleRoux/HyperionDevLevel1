# Request the user to enter the name of 3 products and their prices
product1 = input("Please enter a product: \n")
price1 = float(input("What is the price of the product?" +
                     " (Add both decimals even if 0) \n"))
product2 = input("Please enter another product: \n")
price2 = float(input("What is the price of the product?" +
                     " (Add both decimals even if 0)\n"))
product3 = input("Please enter your final product: \n")
price3 = float(input("What is the price of the product?" +
                     " (Add both decimals even if 0)\n"))

# Calculate the total price of all items and average price per item
total_price = round(price1 + price2 + price3 ,2)
average_price = round((total_price)/3, 2)

# Print results to console
print(f"""The Total of {product1}, {product2}, {product3} is
R{total_price} and the averageprice per item is R{average_price}""")


