"""Defined a function that uses recursion to determine the largest number
in a list. The list gets sliced in every recursion untill it has a single
value then returns that value. Then each first value in every new sliced
list gets compared to the last returned value, returning the largest
between the 2 again and repeating the process which always return the
largest value."""
def largest_number(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        if num_list[0] > largest_number(num_list[1:]):
            return num_list[0]
        else:
            return largest_number(num_list[1:])
    
print(largest_number([3, 1, 6, 8, 2, 4, 5]))
