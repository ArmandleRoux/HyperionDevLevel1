# Import random module for use of randrange()
import random

# Decalre list of jokes. Joke resource https://www.rd.com/list/short-jokes/
# Print random jokes from list to console
jokes = ["Why did the chicken cross the road? \nTo get to the other side",
         "What's the best thing about switzerland? \n"
         "I dont know but the flags a huge plus!",
         "Why is 6 afraid of 7? \nBecause 7, 8 ,9!",
         "What do you call a fish with no eyes? \nA Fsh",
         "I invented a new word! \nPlagiarism",
         "Why do we tell actors to break a leg? \n"
         "Because every play has a cast",
         "Did you hear about the actor who fell through the floorboards? \n"
         "He was just going through a stage.",
         "Did you hear about the claustrophobic astronaut? \n"
         "He just needed a little space.",
         "Why don\’t scientists trust atoms? \n"
         "Because they make up everything."]

print("-"*80)
print(random.choice(jokes))
print("-"*80)