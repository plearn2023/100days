# here we swapping variables of a and b.
# it is same as, you have glass of milk and cup of tea
# you need to swap them. You cannot do so, unless you have additional cup or glass

# 🚨 Don't change the code below
a = input("a: ") # milk cup
b = input("b: ") # tea cup
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# below is my code
# c = a
# d = b
# a = d
# b = c

# below much more logically, because you need just one additional cup or glass
# so you need only one additional variable

c = a # we switch milk cup into another cup, milk cup is empty (ideally)
a = b # we moved tea into milk cup. so tea cup is empty.
b = c # we moved milk (c) into tea cup (b)

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print(" we swapped")
print("a: " + a)
print("b: " + b)
