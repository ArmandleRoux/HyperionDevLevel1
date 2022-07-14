# Request user to enter a sentence
str_manip = input("Please type a sentence: \n")
# Print length of sentence to console
print(len(str_manip))
# Print sentence to console with all the characters that are the same as the
# last character in the sentence replaced with "@"
print(str_manip.replace(str_manip[-1], "@"))
# Print to console the last 3 characters of the sentece backward
print(str_manip[-1: -4: -1])
# Print to console the first 3 characters of the sentence concatenated
# with the last 2 characters of the sentence
print(str_manip[0:3:1] + str_manip[len(str_manip)-2::1])
