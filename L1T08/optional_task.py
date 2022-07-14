# Request input from user to find out what type of employee they are (Salesperson/Manager)
employee_type = input("Are you a salesperson of manager? Type S or M\n").upper()

# If employee is a manager request input for hours worked and calculate wage
# else if employee is a salesperson request input for their gross sles and calculate wage
if employee_type == "M":
    hours_worked = int(input("How many hours have you worked this month? \n"))
    monthly_wage = hours_worked * 40
    print(f"Your monthly wage is R{monthly_wage}")
else:
    gross_sales = float(input("What is your gross sales for the month?"))
    monthly_wage = round(2000 + (gross_sales * 8 / 100), 2)
    print(f"Your monthly wage is R{monthly_wage}")
                            
