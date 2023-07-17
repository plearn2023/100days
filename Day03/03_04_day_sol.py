# Code challenge - Pizza Order - it is the actual solution
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

# as a first customer will select the pizza size.
# we do this using if, elif
# first if block
bill=0
if size=="S":
    bill +=15
elif size=="M":
    bill +=20
else: # when user enter other than M or S, it will L by default
    bill +=25

if add_pepperoni=="Y": # need pepperoni
    if size=="S": # since size matters, we validate size
        bill +=2
    else: # as long size is not small, price remains same i.e. $3. Else is used
        bill +=3
if extra_cheese=="Y": # does not depend upon size.
    bill +=1
    # else is not required. Bill value does not changes, when it is "N"
# else is not required, because bill value will come from # if block
print(f"Your final bill is: ${bill}.")   
    
    
    