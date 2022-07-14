# Request input form user to provide a sentence and characters that the user
# would like to have removed
sentence = input("Please enter a sentence: \n").lower()
strip_characters = input("Which characters whould you like to remove? " +
                         "(seperate each character with a ',')\n"
                         ).replace(" ", "")

# Check for each character in the sentence and remove it using replace()
for char in strip_characters:
    sentence = sentence.replace(char, "")

# Clean sentence if there is extra spaces at the beginning or end of the
# sentence after character removal using strip() and print result to console
sentence = sentence.strip()
print(sentence)
