from datetime import datetime
present = datetime.now()
print (present)  # current date and time

print (present.year)  # current year

present = datetime.now()
print (present.strftime('%B'))  # Month of the year

import datetime
print(datetime.date(2020, 7, 7).isocalendar()[1])  # Week number of the year

print (present.weekday())  # Weekday of the week

from datetime import datetime
present = datetime.now()
print (present.strftime('%-j'))  # Day of the year