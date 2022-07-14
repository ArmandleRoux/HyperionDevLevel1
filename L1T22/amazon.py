# Defines function to calculate maximum between numbers
def maximum(numbers):
    max_number = max(numbers)
    new_line = f"The {data[0]} of {numbers} is {max_number}.\n"
    return new_line

# Defines function to calculate minimum between numbers    
def minimum(numbers):
    min_number = min(numbers)
    new_line = f"The {data[0]} of {numbers} is {min_number}.\n"
    return new_line

# Defines function to calculate average between numbers    
def average(numbers):
    average = round(sum(numbers)/len(numbers), 2)
    new_line = f"The {data[0]} of {numbers} is {average}.\n"
    return new_line

# Defined function to determine position of percentile
# and return the percentile number
def percentile(percentage, numbers):
    percentile_pos = round((percentage/100) * len(numbers)) -1
    percentile = numbers[percentile_pos]
    new_line = (f"The {data[0][1:]}th percentile of {numbers}"
    f" is {percentile}.\n")
    return new_line

# Defined a function to calculate the sum of the numbers
def sum_of(numbers):
    sum_of_numbers = sum(numbers)
    new_line = f"The {data[0]} of {numbers} is {sum_of_numbers}.\n"
    return new_line
    
    
    
# With use of functions calculate min, max, average, percentile and sum of
# numbers and output data to "output.txt" file
with open("input.txt", "r+", encoding='utf-8-sig') as input_file:
    new_line = ""
    for line in input_file:
        data = line.split(":")
        numbers = data[1].replace("\n", "").split(",")
        for i, num in  enumerate(numbers): numbers[i] = int(num)
        with open("output.txt", "a") as output_file:
            if data[0].lower() == "min": output_file.write(minimum(numbers))
            elif data[0].lower() == "max": output_file.write(maximum(numbers))
            elif data[0].lower() == "avg": output_file.write(average(numbers))
            elif data[0][0].lower() == "p":
                output_file.write(percentile(int(data[0][1:]), numbers))
            elif data[0].lower() == "sum": output_file.write(sum_of(numbers))
            

