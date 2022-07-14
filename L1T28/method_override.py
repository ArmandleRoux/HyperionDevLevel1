class Adult:
    """Class containing attriutes of a person.
    
    Attributes:
    name (string): Name of person.
    age (int): Age of person.
    hair_colour(string): Hair colour of person.
    eye_color(string): Eye colour of person."""
    
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
        
    def can_drive(self):
        """Prints object name and that the are old enough to drive"""
        print(self.name + " you are old enough to drive")
        
class Child(Adult):
    """This is a subclass of Adult with all the same attributes.
    
    Attributes:
    name (string): Name of person.
    age (int): Age of person.
    hair_colour(string): Hair colour of person.
    eye_color(string): Eye colour of person."""
    
    def can_drive(self):
        """Prints object name and that they are not old enough to
        drive"""
        print(self.name + " you are not old enough to drive.")
        
name = input("Enter your name: \n")
age = int(input("Enter your age: \n"))
hair_colour = input("Enter your hair colour: \n")
eye_colour = input("Enter your eye colour: \n")
        
if age > 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)
    
person.can_drive()
