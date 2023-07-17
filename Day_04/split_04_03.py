# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

persons=len(names)
# because array starts from 0, you have to use -1
luckyperson=random.randint(0,persons - 1)
print(f"{names[luckyperson]} is going to buy the meal today!")
print(random.choice(names))