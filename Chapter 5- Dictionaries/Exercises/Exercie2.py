# Exercise 2: Glossary:

"""A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call
it a glossary.
* Think of five programming words you’ve learned about in the previous chapters. Use these words as the
keys in your glossary, and store their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word followed by a 
colon and then its meaning, or print the word on one line and then print its meaning indented on a second
line. Use the newline character (\n) to insert a blank line between each word-meaning pair in 
your output."""

glossary = {
    "variable": "A named storage location in computer memory that contains a value.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A programming construct that repeats a group of statements while a condition is true.",
    "dictionary": "A data structure in Python that stores key-value pairs.",
    "conditional statement":
"A programming construct that performs different actions based on whether a condition is true or false."
}

for word, meaning in glossary.items():
    print(f"{word.capitalize()}: {meaning}\n")


