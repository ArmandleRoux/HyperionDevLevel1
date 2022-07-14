# Declare 2 lists to read number from file to
num_list1 = []
num_list2 = []

# Open file1 and read numbers to num_list1
with open("numbers1.txt", "r") as num_file1:

    for line in num_file1:
        num_list1.append(line.replace("\n", ""))


# Open file2 and read numbers to num_list2
with open("numbers2.txt", "r") as num_file2:

    for line in num_file2:
        num_list2.append(line.replace("\n", ""))

# Declare a list to add all numbers together and sort list with sort()
# I found out how to use key=int in sort() from python documentation
all_numbers_list = num_list1 + num_list2
all_numbers_list.sort(key=int)

# Write the sorted number list to a new file
with open("all_numbers.txt", "w") as all_num_file:
    for num in all_numbers_list:
        all_num_file.write(num + "\n")

