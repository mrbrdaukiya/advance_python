# datetime Module

from datetime import datetime
dt1 = datetime(year=2023, month=9, day=14)
dt2 = datetime(year=2022, month=8, day=25, hour=10, minute=51, second=11)
dt3 = datetime(2021, 7, 20)
dt4 = datetime(2020, 6, 15, 12, 30)

print(dt1)
print()
print(dt2)
print()
print(dt3)
print()
print(dt4)
print("-----------------------------------")
print(dt1.year)

print("***********************************************************")

# Date and Time Class method

from datetime import datetime
ct = datetime.now()
print(ct)

ct = datetime.today()
print(ct)