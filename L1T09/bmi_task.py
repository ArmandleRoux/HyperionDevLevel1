# Request user input to provide their body weight and height
weight = float(input("Please enter your weight in kg: \n"))
height = float(input("Please enter your height in meter: \n"))

# Calculate the BMI with input from user
bmi = round(weight/height**2, 2)

# Check if BMI is above 30, between 25 and 30, between 18.5 and
# 25 or below 18.5 and print appropriate response to console
if bmi >= 30:
    print(f"Your BMI is {bmi}. You are obese.")
elif bmi >= 25:
    print(f"Your BMI is {bmi}. You are overweight")
elif bmi >= 18.5:
    print(f"Your BMI is {bmi}. This is normal.")
else:
    print(f"Your BMI is {bmi}. You are underweight")
    


