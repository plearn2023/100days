# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=weight/(height ** 2)
BMI_rounded=(round(BMI))

if BMI_rounded < 18.5:
    print (f"Your BMI is {BMI_rounded}, you are underweight.")
elif BMI_rounded < 25:
    print (f"Your BMI is {BMI_rounded}, you have a normal weight.")
elif BMI_rounded < 30:
    print (f"Your BMI is {BMI_rounded}, you are slightly overweight.")
elif BMI_rounded < 35:
    print (f"Your BMI is {BMI_rounded}, you are obsese.")
else :
    print (f"Your BMI is {BMI_rounded}, you are clinically obese.")
    