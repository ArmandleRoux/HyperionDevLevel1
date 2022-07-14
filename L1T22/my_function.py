# Defined a function that prints out all the days of the week to console
def days_of_week():
    dow = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday",
           "Saturday", "Sunday"]
    for day in dow:
        print(day)
 
 
# Defined a function that will change every second word into "Hello"        
def word_replace(sentence):
    words = sentence.split(" ")
    new_sentence =""
    for i, word in enumerate(words):
        if i%2 != 0:
            words[i] = "Hello"
    for word in words:
        new_sentence += word + " "
    print(new_sentence)

# Declared a string sentence ti test word_replace function and 
# call days_of_week to test if function is working
test_sentence = "I live in a town called Pittsburg"

days_of_week()    
word_replace(test_sentence) 