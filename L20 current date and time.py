from datetime import date , datetime

# calling the today
# funtion of date class
today = date.today()
now = datetime.now()

print("todays date is ", today)
print("current date and time is", now)
print()

#printing todays date
print("date componets", today.year, today.month, today.day)
print()