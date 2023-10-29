# Exercise 5: USB Shopper :
"""A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and 
wants as many as she can get for £50. They are £6 each. Write a programme that calculates 
how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise.  """

budget=50
USB_cost=6
num_USB=budget/USB_cost
num_USB=int(num_USB)
remainder=budget-(num_USB*USB_cost)
print("Number of USB that can be bought:",num_USB)
print("Money left over:",remainder)