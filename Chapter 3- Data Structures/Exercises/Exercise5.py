# Exercise 5: Change Guest List:

"""You just heard that one of your guests can’t make the dinner, so you need to send out a new set of
 invitations. You’ll have to think of someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the
 name of the guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you
 are inviting.
•Print a second set of invitation messages, one for each person who is still in your list."""

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

