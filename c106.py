a = 10
b = 0
try:
    d = a/b
    print(d)
except ZeroDivisionError:
    print("Division by Zero Not Allowed")

print("Rest Of The Code")

print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError:
    print("Division by Zero Not Allowed")

print("Rest Of The Code")




print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError:
    print("Division by Zero Not Allowed")

else:
    print("Inside Else")

print("Rest Of The Code")






print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError:
    print("Division by Zero Not Allowed")

else:
    print("Inside Else")

finally:
    print("Inside Finally")

print("Rest Of The Code")





print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    d = a/b
    print(d)
    print("Inside Try")
except ZeroDivisionError as obj:
    print(obj)


print("Rest Of The Code")




print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    d = a/b 
    print(d)
    print("Inside Try")
except ZeroDivisionError as obj:
    print(obj)

except NameError as ob:
    print(ob)


print("Rest Of The Code")





print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    # d = a/g 
    print(d)
    print("Inside Try")
except (ZeroDivisionError, NameError )as obj:
    print(obj)



print("Rest Of The Code")





print("------------------------------------------")

a = 10
# b = 5
b = 0
try:
    # d = a/g 
    print(d)
    print("Inside Try")
except:
    print('Exception Handler')



print("Rest Of The Code")
