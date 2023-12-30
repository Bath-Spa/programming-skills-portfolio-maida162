# Exercise 5: Pets:

"""Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include
the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop 
through your list and asyou do, print everything you know about each pet."""

pet1 = {'kind': 'dog', 'owner': 'Alice'}
pet2 = {'kind': 'cat', 'owner': 'Bob'}
pet3 = {'kind': 'parrot', 'owner': 'Charlie'}
pet4 = {'kind': 'rabbit', 'owner': 'David'}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
    print(f"Kind: {pet['kind'].capitalize()}")
    print(f"Owner: {pet['owner'].capitalize()}")
    

    


