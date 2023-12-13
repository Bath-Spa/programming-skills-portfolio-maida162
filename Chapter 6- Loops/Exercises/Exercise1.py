# Exercise 1: Pizza Toppings:

"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
As they enter each topping,
print a message saying you’ll add that topping to their pizza."""

pizza_toppings = []

while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() == 'quit':
        break  
    pizza_toppings.append(topping)

    print(f"{topping.capitalize()} will be added to your pizza.")

print("\nYour pizza will have the following toppings:")
for topping in pizza_toppings:
    print("- " + topping.capitalize())
