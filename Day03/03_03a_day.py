# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# you need a float chart to put such logic in place. At beginner like me.
result=year % 4
result_100=year % 100
result_400=year % 400
if(result == 0): # if true, then go and check result_100
    if(result_100 == 0): # if true, then go and check result_400
        if(result_400 == 0): # this is double if condition.
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")