# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result=year % 4
result_100=year % 100
result_400=year % 400
# print(result)
# print(result_100)
# print(result_400)
if(result == 0):
    if(result_100 != 0):
        print("This is leap year")
    elif(result_400 == 0):
        print("This is leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")