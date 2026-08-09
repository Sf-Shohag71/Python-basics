class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")
        
car1 = Car()
# car1.start()

# Create account class with 2 attributes -  balance and account number
# create methods for debit, credit and check balance
class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.account_number = acc_no
    
    def debit(self, amount):
        self.balance -= amount
        print("BDT.", amount, "debited")
        print("Current balance: BDT. ", self.check_balance())
        
    def credit(self, amount):
        self.balance += amount
        print("BDT.", amount, "credited")
        print("Current balance: BDT.", self.check_balance())

    def check_balance(self):
        return self.balance
    
acc1 = Account(10000, 54321)
acc1.debit(1000)