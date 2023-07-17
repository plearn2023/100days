# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = "Kim Kardashian"
name2 = "Kanye West"
# 🚨 Don't change the code above 👆
 
#Write your code below this line 👇
to_lower_names = name1.lower() + name2.lower()  
T = to_lower_names.count('t')
R = to_lower_names.count('r')
U = to_lower_names.count('u')
E = to_lower_names.count('e')
Ttotal = T + R + U + E
print(Ttotal)
 
L = to_lower_names.count('l')
O = to_lower_names.count('o')
V = to_lower_names.count('v')
E = to_lower_names.count('e')
Ltotal = L + O + V + E 
 
total = str(Ttotal) + str(Ltotal) 
loveScore = int(total)
print(loveScore)