# Exercise 3: Glossary 2:

"""Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by
replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. 
When you’re sure that your loop works, add five more Python terms to your glossary.When you run your
program again, these new words and meanings should automatically be included in the output."""

glossary = {
    "variable": "A named storage location in computer memory that contains a value.",
    "function": "A reusable block of code that performs a specific task.",
    "loop": "A programming construct that repeats a group of statements while a condition is true.",
    "dictionary": "A data structure in Python that stores key-value pairs.",
    "conditional statement": 
"A programming construct that performs different actions based on whether a condition is true or false."
}

glossary["module"] = "A file containing Python definitions and statements."
glossary["list comprehension"] = "A concise way to create lists in Python."
glossary["exception"] = "An event that occurs during the execution of a program and disrupts the normal flow of instructions."
glossary["tuple"] = "An immutable ordered collection of elements in Python."
glossary["method"] = "A function that is associated with an object and can be called on that object."

for word, meaning in glossary.items():
    print(f"{word.capitalize()}: {meaning}\n")

