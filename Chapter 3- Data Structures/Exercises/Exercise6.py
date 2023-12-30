# Exercise 6: Shrinking Guest List

"""You just found out that your new dinner table won’t arrive in time for the dinner, and you have space 
for only two guests.
•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can
 invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each
 time you pop a name from your list, print a message to that person letting them know you’re sorry you
 can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. Print your list to make
 sure you actually have an empty list at the end of your program."""

guest_list = ["Leonardo diCaprio", "Alama Iqbal", "Imran Khan"]
print("Dear " + guest_list[0] + """, you are invited to dinner. Your acting skills are amazing and you
      are a wonderful person.""")
print("Dear " + guest_list[1] + """, you are invited to dinner. your poetry is incredible we want to
       listen it.""")
print("Dear " + guest_list[2] + """, you are invited to dinner. Your leadership and dedication to justice
       have left a lasting impact.""")
guest_cannot_make_it = guest_list.pop(1)
print("\nUnfortunately, " + guest_cannot_make_it + " can't make it to the dinner.")
new_guest = "Marie Curie"
guest_list.insert(1, new_guest)
print("\nUpdated Invitation List:")
print("Dear " + guest_list[0] + """, you are invited to dinner. Your acting skills are amazing and you
      are a wonderful person.""")
print("Dear " + guest_list[1] + """, you are invited to dinner. Your groundbreaking work in radioactivity
       is truly inspiring.""")
print("Dear " + guest_list[2] + """, you are invited to dinner. Your leadership and dedication to justice
       have left a lasting impact.""")

print("Due to a delay, the new dinner table won't arrive on time, and only two guests can be invited.")

# Use pop() to remove guests until only two names remain
while len(guest_list) > 2:
    removed_guest = guest_list.pop()
    print(f"Sorry, {removed_guest}, I can't invite you to dinner.")

# Print messages to the two remaining guests
for remaining_guest in guest_list:
    print(f"{remaining_guest}, you're still invited to dinner.")

# Use del to remove the last two names and print the empty list
del guest_list[:]
print("The guest list is now empty:", guest_list)


