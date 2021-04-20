class bank_application:
    """"this application by rakesh"""
    Bank_Name = "Rakesh-Bank"
    def __init__(self, name, balance= 0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance+amount
        print("After deposit, the balance: ", self.balance)

    def withdraw(self, amount):
        if amount>self.balance:
            print("requested amount is not possible")
        else:
            self.balance = self.balance-amount
            print("after withdraw", self.balance)

print("Welcome to ", bank_application.Bank_Name)
name = input("Enter your name: ")
c = bank_application(name)
while True:
    print("d-deposit\n w-withdraw\ne-exit")
    opt = input("enter your option")
    if opt.lower() =="d":
        depo = float(input("Enter your amount to be deposited"))
        c.deposit(depo)
    elif opt.lower() =='w':
        amount= float(input("Enter amount to withdraw :"))
        c.withdraw(amount)
    elif opt.lower() =='e':
        print("Thanks for banking")
        break
    else:
        print("please choose valid statement")


























