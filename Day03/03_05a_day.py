# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combinenames=name1.lower() + name2.lower()
checkT=combinenames.count("t")
checkR=combinenames.count("r")
checkU=combinenames.count("u")
checkE=combinenames.count("e")
TRUECOUNT=checkT+checkR+checkU+checkE

checkL=combinenames.count("l")
checkO=combinenames.count("o")
checkV=combinenames.count("v")
checkEE=combinenames.count("e")
LOVECOUNT=checkL+checkO+checkV+checkEE

#print(str(TRUECOUNT)+str(LOVECOUNT))
LOVECHECK=int(str(TRUECOUNT)+str(LOVECOUNT))

if LOVECHECK <=10 or LOVECHECK >=90:
    print(f"Your score is {LOVECHECK}, you go together like coke and mentos.")
elif LOVECHECK >=40 and LOVECHECK <=50:
    print(f"Your score is {LOVECHECK}, you are alright together.")
else:
    print(f"Your score is {LOVECHECK}.")