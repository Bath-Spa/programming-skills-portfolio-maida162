# Exercise 4:  Large Shirts:

"""Modify the make_shirt() function so that shirts are large by default with a message that reads I love 
Python. Make a large shirt and amedium shirt with the default message, and a shirt of any size with 
a different message."""

def make_shirt(size="large", message="I love Python"):
    """Prints a sentence summarizing the size and message on a shirt."""
    print(f"Made a shirt of size {size} with the message: '{message}'")

make_shirt()

make_shirt(size="medium")

make_shirt(size="small", message="Python is fun!")

