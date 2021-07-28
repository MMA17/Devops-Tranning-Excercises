import random

class bankAccount:
    balance = 0

    def __init__(self, balance) -> None:
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Nap so tien " + str(amount) + " Tai khoan co: " + str(self.balance))

class VPBank(bankAccount):
    def withdraw(self, amount):
        self.balance = self.balance - amount - amount*0.1
        print("VPB Rut so tien " + str(amount) + " Tai khoan co: " + str(self.balance))

class TechcomBank(bankAccount):
    def withdraw(self, amount):
        self.balance = self.balance - amount - amount*0.1
        print("TCB Rut so tien " + str(amount) + " Tai khoan co: " + str(self.balance))

#VPBank(12000).withdraw(1000)

def run():
    list  = [(VPBank(10000), 3200), (TechcomBank(23000), 9555), (TechcomBank(50000), 33000)]
    for x in list:
        temp = random.randint(0,1)
        #print (temp)
        if temp == 1:
            x[0].deposit(int(x[1]))
        else:
            x[0].withdraw(int(x[1]))

run()
