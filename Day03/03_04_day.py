# Code challenge - Pizza Order
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

if size=="S":
    # print("Small Pizza costs $15")
    small_p_prize=15
    if add_pepperoni=="Y":
        small_p_prize +=2
    if extra_cheese =="Y":
        small_p_prize +=1
        print(f"Your final bill is: ${small_p_prize}.")
    else:
        print(f"Your final bill is: ${small_p_prize}.")
elif size=="M":
    # print("Small Pizza costs $15")
    medium_p_prize=20
    if add_pepperoni=="Y":
        medium_p_prize +=3
    if extra_cheese =="Y":
        medium_p_prize +=1
        print(f"Your final bill is: ${medium_p_prize}.")
    else:
        print(f"Your final bill is: ${medium_p_prize}.")
elif size=="L":
    # print("Small Pizza costs $15")
    large_p_prize=25
    if add_pepperoni=="Y":
        large_p_prize +=3
    if extra_cheese =="Y":
        large_p_prize +=1
        print(f"Your final bill is: ${large_p_prize}.")
    else:
        print(f"Your final bill is: ${large_p_prize}.")