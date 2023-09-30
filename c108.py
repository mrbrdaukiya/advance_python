# User Defined Exception

class BalanceExceptionError(Exception):
    pass

def checkbalance():
    money = 10000
    withdraw = int(input('Enter withdraw Money :'))
    try:
        balance = money - withdraw
        if(balance<=2000):
            raise BalanceExceptionError('Insufficient Balance')
        print("Avalibale Balance :",balance)
    except BalanceExceptionError as be:
        print(be)

# checkbalance()

print("-------------------------------------------")


class BalanceExceptionError(Exception):
    pass

def checkbalance():
    money = 10000
    withdraw = int(input('Enter withdraw Money :'))
    balance = money - withdraw
    if(balance<=2000):
        raise BalanceExceptionError('Insufficient Balance')
    print("Avalibale Balance :",balance)
    

try:
    checkbalance()
except BalanceExceptionError as be:
        print(be)