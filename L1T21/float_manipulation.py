# Import math libriry for use of sum(),min(),max()
import math

# Request input from user to provide 10 numbers and read numbers to 
# declared list.
# Use received data to determine the sum, maximum, minimum,
# average and median of the numbers and print each result to console
numbers = []
print("Please provide 10 numbers")
for i in range(0,10):
    numbers.append(float(input("Type in a number and press enter:")))   

print(f"Sum of numbers: \t {sum(numbers)}")
print(f"Maximum:        \t {max(numbers)}")
print(f"Minimum:        \t {min(numbers)}")

average = round(sum(numbers)/len(numbers), 2)
print(f"Average:        \t {average}")

numbers = sorted(numbers)
median_pos = int(len(numbers)/2)
median = round((numbers[median_pos -1]+numbers[median_pos])/2, 2)    
print(f"Median:         \t {median}")