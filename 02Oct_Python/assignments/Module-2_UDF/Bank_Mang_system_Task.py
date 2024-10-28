#A/C opening

def Account_opening(*data):
    print("Enter your Name:",data[0])
    print("Enter your Type:",data[1])
    print("Enter your Number:",data[2])

nm = input("Enter your Name:")
typ = input("Enter your Type:")
num = input("Enter your Number:")

Account_opening(nm,typ,num)

#Deposit

DAmnt = int(input("Enter Deposit amount:"))

if(DAmnt < 2000):
    print("Deposit Amount should be more than 2000")
else:
    print(f"{DAmnt} is deposited in your Account.")

#total balance

TotalBalance = DAmnt

#withdraw 

WAmnt = int(input("Enter Withdraw amount:"))

if(WAmnt > TotalBalance):
    print(f"{WAmnt} is more than balance present in your account.")
else:
    print(f"{WAmnt} is withdrawed.")

#statement

def statement():

    print(Account_opening(nm,typ,num))
    print(TotalBalance)





