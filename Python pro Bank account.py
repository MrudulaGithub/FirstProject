class BankAccount(object):
    balance = 0
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return "%s's account.Balance: $%.2f" %(self.name,self.balance)

    def show_balance(self):
        print "Your Account Balance is: $%.2f" %(self.balance)

    def deposit(self,amount):
        if amount <=0:
            print "Invalid deposit"
            return
        else:
            print "Your deposit amount: $%.2f" %(amount)
            self.balance += amount
            self.show_balance()

    def withdraw (self,amount):
        if amount >= self.balance:
            print "Exceeding account balance"
            return
        else:
            print "Withdrawal amount: $%.2f" %(amount)
            self.balance -= amount
            self.show_balance()

my_account = BankAccount("Mrudula")
print my_account
my_account.show_balance()
my_account.deposit(1000)
my_account.withdraw(500)
print my_account

