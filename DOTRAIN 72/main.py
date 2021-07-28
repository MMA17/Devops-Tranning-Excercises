import random

class bankAccount:
    bankName = ""
    amount = 0
    balance = 10000

    def __init__(self, bankName: str, amount: int):
        #print("Gan gia tri")
        self.bankName = bankName
        self.amount = amount
        
    def deposit(self):
        self.balance += int(self.amount)
        print ("Nap so tien: " + str(self.amount))
        print ("Tai khoan ban co: %s" %(self.balance))

    def withdraw(self):
        if (self.bankName == "VPB"):
            self.balance = self.balance - int(self.amount) - int(self.amount)*0.05
            print("Rut so tien: " + str(self.amount))
            print ("Tai khoan ban co: %s" %(self.balance))
        if (self.bankName == "TCB"):
            self.balance = self.balance - int(self.amount) - int(self.amount)*0.1
            print("Rut so tien: " + str(self.amount))
            print ("Tai khoan ban co: %s" %(self.balance))

def run():
    listBankAccount = [("VPB", 7000), ("TCB", 2500), ("TCB", 5000)]
    for x in listBankAccount:
        temp = random.randint(0,1)
        #print (temp)
        if temp == 1:
            bankAccount(x[0], int(x[1])).deposit()
        else:
            bankAccount(x[0], int(x[1])).withdraw()

run()
