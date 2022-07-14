def hotel_cost():
    """Request input from user to provide total nights they will stay
    at hotel and return total price of hotal stay.
    
    Returns:
        (float): Total price of hotel stay.
    """
    draw_line()
    total_nights = int(input("How many nights will you be staying at "
                                    "the hotel?\n>"))
    return total_nights * 199.99


def plane_cost():
    """Request input from user ot provide a city from the list. Check
    if city is in the list and return price of flight to given city.
    
    Returns:
        (float) : Price of the plane ticket to given city
    """
    draw_line()
    city = (input("What city are you going to?\n--------------"
             "\n|Pretoria    |\n|Durban      |\n|Cape Town   |\n"
             "|Bloemfontein|\n|George      |\n|Johannesburg|\n" 
             "|Kimberley   |\n--------------\n>").lower()
            ).replace(" ", "")
    city_dict = {"pretoria": 499.99,
                 "durban": 799.99,
                 "capetown": 1199.99,
                 "bloemfontein": 599.99,
                 "george": 1399.99,
                 "johannesburg": 499.99,
                 "kimberley": 899.99}
    if city in city_dict:
        return city_dict[city]


def car_rental():
    """Request input from user to provide amount off days they will be
    renting a car calculates the total cost of car rental.
    
    Returns:
        (int): Price of car rental.
    """
    draw_line()
    total_days = int(input("How many days will you be renting a car?\n>"))
    return total_days * 99


def holiday_cost(hotel_nights, city, car_days):
    """Calculate total cost of holiday and returns it."""
    return round(hotel_nights + city  + car_days, 2)


def draw_line():
    """Draws a line to console"""
    print("-"*80)
    

"""Main Program
Call the functions hotel_cost, plane_cost, car_rental_cost and
holiday_cost and print results to screen
"""

hotel_price = hotel_cost() 
plane_price = plane_cost()
car_price = car_rental()
total_price =holiday_cost(hotel_price, plane_price, car_price)

draw_line()
print(f"Price for hotel:        \tR{hotel_price}\n" 
      f"Price for Plane ticket: \tR{plane_price}\n" 
      f"Price for car rental:   \tR{car_price}\n\n"
      f"The total price for your holiday is: \tR{total_price}")
draw_line()
