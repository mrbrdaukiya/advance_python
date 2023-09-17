# Calculate Age from time Method

from datetime import date

dob = date(1996, 6, 8)

t = date.today()

age = t.year - dob.year - ((t.month, t.day)< (dob.month, dob.day))

print(age)