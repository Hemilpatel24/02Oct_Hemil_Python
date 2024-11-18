import random
class Account_opening:
    name=""
    type=""
    amnt=0

    def getdata(self):
        self.num = random.randint(1000,9999)
        self.name = input("==================\nEnter your Name:")
        self.type = input("Enter your Account type:")
    
class deposit(Account_opening):

    def enter_amnt(self):
        self.amnt = int(input("Enter Deposit ammount:"))
        if(self.amnt<2000):
            print("Min deposit should be 2000 or >")
        else:
            print(f"=================\n{self.amnt} is Deposited.\n===================")
        
class Withdrawl(deposit):

    def withdraw_amount(self, amount):
        
        if amount<=self.amnt:
            self.amnt-=amount
            print(f"{amount} Amount Withdrawn and Amount left is = {self.amnt}")

class statement(Withdrawl):

    def get_statement(self):
        print(f"Account Number : {self.num}")
        print(f"Account Name : {self.name}")
        print(f"Account Type : {self.type}")
        print(f"Account Balance : {self.amnt}")
        

account = statement()
account.getdata()
account.enter_amnt()
account.withdraw_amount(1000)
account.get_statement()


    


        
