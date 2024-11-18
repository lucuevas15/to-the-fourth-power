"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Variable inputs created
numChar = int(input("please enter number of character: "))
woodType = input("please enter wood type: ")
color = input("please enter sign color: ")

# # Base charge for this sign.
charge = 35


# Assignment and if statements
if numChar > 5 : charge += (numChar - 5) * 4

if woodType == 'oak': charge += 20
else : charge += 0

if color == 'gold': charge += 15
else : charge += 0 

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
