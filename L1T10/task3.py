# Request user imput to provide the times of the contestant for all 3 events
swimming_time = int(input("Enter swim time:(min) \n"))
cycling_time = int(input("Enter cycling time:(min) \n"))
running_time = int(input("Enter run time:(min) \n"))

# Calculate the total time of contestant
total_time = swimming_time + cycling_time + running_time

# Check to see which reward will received according to total_time and print
# appropriate message to console
if total_time <= 100:
    print("Congratulations you have received Provincial Colors!")
elif total_time <= 105:
    print("Congratulations you have received Provincial Half Colors!")
elif total_time <= 110:
    print("Congratulations you have received a Provicial Scroll!")
else:
    print("You unfortunately do not qualify for a reward.")
