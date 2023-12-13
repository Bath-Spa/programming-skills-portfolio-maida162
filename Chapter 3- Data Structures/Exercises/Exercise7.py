# Exercise 7: Seeing the World :

"""Think of at least five places in the world you’d like to visit.
•	 Store the locations in a list. Make sure the list is not in alphabetical order.
•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a
     raw Python list.
•	 Use sorted() to print your list in alphabetical order without modifying the actual list.
•	 Show that your list is still in its original order by printing it.
•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the
     original list.
•	 Show that your list is still in its original order by printing it again.
•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its
     original order.
•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its
     order has been changed.
•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show
     that its order has changed."""

places_to_visit = ["Tokyo", "Paris", "New York",  "Sydney"]

# Print the list in its original order
print("Original Order:", places_to_visit)
# Use sorted() to print the list in alphabetical order without modifying the original list
print("Sorted Order:", sorted(places_to_visit))
# Show that the original list is still in its original order
print("Original Order (after using sorted()):", places_to_visit)
# Use sorted() to print the list in reverse alphabetical order without changing the order of the original list
print("Reverse Sorted Order:", sorted(places_to_visit, reverse=True))
# Show that the original list is still in its original order
print("Original Order (after using sorted() with reverse=True):", places_to_visit)
# Use reverse() to change the order of the list
places_to_visit.reverse()
print("Reversed Order:", places_to_visit)
# Use reverse() again to change the order back to the original
places_to_visit.reverse()
print("Back to Original Order:", places_to_visit)
# Use sort() to change the list to alphabetical order
places_to_visit.sort()
print("Alphabetical Order:", places_to_visit)
# Use sort() again to change the list to reverse alphabetical order
places_to_visit.sort(reverse=True)
print("Reverse Alphabetical Order:", places_to_visit)

