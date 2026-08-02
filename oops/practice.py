class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs", amount ,"was debited")
        print("total balance = ",self.get_bal())

    def credit(self,amount):
        self.balance += amount
        print("Rs", amount ,"was credited")
        print("total balance = ",self.get_bal())

    def get_bal(self):
        return self.balance
        
acc1 = account (600000,836647590)
acc1.debit (10000)
acc1.credit(5000)