# this code is just for me to learn
#Write your code below this line 👇
name1 = "Kanye West".lower()
name2 = "Kim Kardashian".lower()
#name1 = name2 + name3
print(name1)
print(name2)
# print(f" this is  e {name1.count('e')}")
# print(name1.count("A"))
name1_count_true=0
name1_count_love=0
# name2
name2_count_true=0
name2_count_love=0

if name1.count("t"):
    name1_count_true +=1
if name1.count("r"):
    name1_count_true +=1
if name1.count("u"):
    name1_count_true +=1
# this logic is wrong because if you have more than "e", 
# it does not count.
if name1.count("e"):
    name1_count_true +=1
print(f"true count of {name1}  is {name1_count_true}")
#  name1 love count
if name1.count("l"):
    name1_count_love +=1
if name1.count("o"):
    name1_count_love +=1
if name1.count("v"):
    name1_count_love +=1
if name1.count("e"):
    name1_count_love +=1
# name2
if name2.count("t"):
    name2_count_true +=1
if name2.count("r"):
    name2_count_true +=1
if name2.count("u"):
    name2_count_true +=1
if name2.count("e"):
    name2_count_true +=1
print(f"true count of {name2}  is {name2_count_true}")
if name2.count("l"):
    name2_count_love +=1
if name2.count("o"):
    name2_count_love +=1
if name2.count("v"):
    name2_count_love +=1
if name2.count("e"):
    name2_count_love +=1
# print(name2_count_love)

print(f"TRUE Count: {name1_count_true+name2_count_true}")
print(f"LOVE Count: {name1_count_love+name2_count_love}")
#print(sum_true)
TRUE_Count=name1_count_true+name2_count_true
LOVE_Count=name1_count_love+name2_count_love

print(str(TRUE_Count)+str(LOVE_Count))