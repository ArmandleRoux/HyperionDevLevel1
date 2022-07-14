'''Defined a definition that that takes a sentence, a substring to
remove from the sentence and then another string to replace the first
substring with. The function then removes the given substring and replaces
it with the second provided string recursively utill the sentence does
not contain the substring  anymore then it returns the sentence'''
def search_replace(sentence, remove_str, replace_str):
    if remove_str not in sentence:
        return sentence
    else:
        return search_replace(sentence.replace(remove_str, replace_str)
                              , remove_str, replace_str)
    
word = input("Please enter a string: ")
substring = input("Please enter the substring you wish to find: ")
replace_with = input("Please enter a string to replace the given substring:")

print(f"Your new string is: {search_replace(word, substring, replace_with)}")
