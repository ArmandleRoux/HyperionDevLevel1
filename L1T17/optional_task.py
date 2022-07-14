# Open file and read contents to variable. While reading content to variable
# count lines with use of total_lines variable
f = open("input.txt", "r") 
content = ""
total_lines = 0
for line in f:
    content += line
    total_lines += 1

# Calculate the total characters and total words in content
total_char = len(content)
total_words = len(content.split(" "))

# Declared list for vowels to make counting easier and a integer to count
# vowels
vowels = "aeiou"
total_vowels = 0

# Determine which characters are vowels and count them
for char in content:
    if char in vowels:
        total_vowels += 1

# Print results to console
print(f"Total characters in file: \t{total_char} \n" 
    f"Total words in file:      \t{total_words} \n"
    f"Total lines in file:      \t{total_lines} \n"
    f"Total vowels in file:     \t{total_vowels} \n")
