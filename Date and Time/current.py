from datetime import datetime
present = datetime.now()
print (present)  # current date and time

print (present.year)  # current year
print (present.month)  # current month
print (present.day)  # current day

print (present.weekday())  # Weekday of the week

present = datetime.now()
print (present.strftime('%A'))  # Day of the week

present = datetime.now()
print (present.strftime('%B'))  # Month of the year

present = datetime.now()
print (present.strftime('%D'))  # Day of the month

present = datetime.now()
print (present.strftime('%-j'))  # Day of the year

present = datetime.now()
print (present.strftime('%w'))  # Week number of the year