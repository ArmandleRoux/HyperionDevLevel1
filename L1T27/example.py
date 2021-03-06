# Welcome to the example file for Object Orientated Programming (Part 1).
# Please ensure that you have read through the task file (pdf) before continuing here as some of
# the examples and explanations assume you have done so.

# ************* HELP *****************
#  REMEMBER THAT YOU IF YOU EVER NEED ANY HELP AT ALL, EMAIL US ON HELP@HYPERIONDEV.COM.
# ************************************

# ==== LET'S OOP! ====

# Breaking our programs into multiple classes (instead of doing everything in one big class) is an essential tool for
# managing bigger tasks with more complexity.

# We'll want our classes to encapsulate the data and the functionality for an object - the blueprint.
# Encapsulate means to enclose, as if in a capsule.
# One of the popular ways of figuring out how to break a complex system into more
# manageable components is to write this information on an index card that is divided into three parts:
# What is the name of the class?
# What responsibilities will it (or the objects we instantiate from it) have?
# What other (types of) objects will it collaborate with?


# =====================================
#  A trivial example of a class
# =====================================

class Cow(object):
    '''
    A triple-quote string is called a docstring and is used to store information
    about the class, function, or file/module in which it is contained.
    It is stored in the 'special variable' __doc__ and may be viewed
    in any of the following ways.

    >>> help(Cow)
    >>> print Cow.__doc__
    >>> cow = Cow()
    >>> help(cow)
    >>> print cow.__doc__

    Documenting the code you write is of fundamental importance.
    Docstrings allow you to somewhat automate the process; there are tools
    like Sphinx and Doxygen that generate documentation from docstrings.
    IDEs like Eclipse can also display them as part of their autocompletion.
    '''
    _noise = 'moo!'
    def __init__(self, color):
        '''
        This is the constructor for the class SimpleCow.
        A constructor creates a new instance of a class (see the introductory reading).

        To instantiate a class with the constructor, you simply call the class name like a function:
        >>> blue_cow = SimpleCow('blue')
        '''
        self.color = color

        

    def make_noise(self):
        '''
        This method prints the cow's noise to the standard output...

        A method is simply a function attached to an object (see reading).
        In Python, methods and properties are accessed with the dot operator:
        >>> blue_cow.make_noise()
        '''
        print(self._noise)

    def set_color(self, new_color):
        '''
        To paint the cow a different color.
        This method is meant to be an example of the way that methods can modify an object's state.

        Get/set methods for object properties are a common sight in object-oriented code,
        but in Python they are not really necessary because Python lacks something called privacy.
        The first expression below is generally considered to be more 'Pythonic' (i.e. idiomatic) than the second:
        >>> blue_cow.color = 'red'
        >>> blue_cow.set_color('red')
        '''
        self.color = new_color

    def get_color(self):
        '''
        This method returns the cow's color.
        '''
        return self.color

    def __cmp__(self, other):
        '''
        This is a comparison special method.  It returns True if the two cows are the same
        color, and false if they are not.
        This strange-looking method is one of the so-called 'special methods'
        that are part of the Python language.
        Some of the special methods, like __del__(),
        have very specific functions.
        Others, like __cmp__, provide the functionality for 'operators'
        like ==, +, -, *, >, etc.  __cmp__ corresponds to the equality comparison
        operator ==.

        In other words, the following expressions are equivalent:
        >>> blue_cow == red_cow
        >>> blue_cow.__cmp__(red_cow)

        And so are these:
        >>> 'a'.__add__('b')
        >>> 'a' + 'b'

        Implementating these methods for custom classes is called 'operator overloading.'.
        An exhaustive if somewhat outdated list of these special methods and their purposes
        may be found at http://docs.python.org/release/2.5.2/ref/specialnames.html.

        In practice, it is often better to avoid operator overloading, as it can lead
        to reduced code clarity and strange bugs if errors are not handled correctly.
        '''
        if self.color == other.color:
            return True
        else:
            return False

    def __str__(self):
        '''
        This special method is called by Python when you use the 'print' command
        on an object.
        >>> print blue_cow
        'blue moo'
        >>> print blue_cow.__str__()
        'blue moo'
        '''
        return self.color + ' ' + self._noise

blue_cow = Cow('blue')
red_cow = Cow('red')

blue_cow.make_noise()

print(red_cow == blue_cow)

blue_cow.set_color('red')
print(red_cow == blue_cow)

# ==== End of Trivial Example ====
