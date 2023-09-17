# Formatting Date and Time

# format code 
# %a 
# %A 
# %d 
# %b 
# %B 
# %m 
# %y 
# %Y 
# %H 
# %I 
# %p 
# %M 
# %S 
# %f 
# %Z 
# %j 
# %U 
# %c 
# %x 
# %X
# %%

from datetime import datetime
dt = datetime.today()
print(dt)
print()

newd1= dt.strftime("%d/%B/%Y")
print(newd1)
print(type(newd1))
print()


newd2= dt.strftime("%d/%b/%Y")
print(newd2)
print()


newd3= dt.strftime("%d-%m-%Y")
print(newd3)
print()



newd4= dt.strftime("%H:%M:%S")
print(newd4)
print()



newd4= dt.strftime("%I:%M:%S")
print(newd4)
print()