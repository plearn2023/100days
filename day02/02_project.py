# Calculate the tip
print("Welcome to the tip calculator.")
total_amount=input("What was the total bill? $")
percentage=input("What percentage tip would you like to give? 10, 12, or 15? 12 ")
no_of_people=input("How many people to split the bill? ")
total_amount_int=int(total_amount)
percentage_int=int(percentage)
no_of_people_int=int(no_of_people)

total_amount_with_tip=(total_amount_int) * (1+(percentage_int/100))
tip_per_person=total_amount_with_tip/no_of_people_int
tip_per_person_two_decimal='{:.2f}'.format(round(tip_per_person))
print(f"${tip_per_person_two_decimal}")

