from datetime import datetime
present = datetime.now()
print (present)  # current date and time

print (present.year)  # current year

present = datetime.now()
print (present.strftime('%B'))  # Month of the year