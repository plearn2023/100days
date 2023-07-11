# current age
age=input("What is your current age? ")
age_int=int(age)
# minus 90 from the current age
time_to_live_years=90 - age_int
# print(time_to_live)
time_to_live_days=time_to_live_years * 365
time_to_live_weeks=time_to_live_years * 52
time_to_live_month=time_to_live_years * 12
message=print(f"You have {time_to_live_days} days, {time_to_live_weeks} weeks, and {time_to_live_month} months left")
print(message)


# change that in to days, weeks and months