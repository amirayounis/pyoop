# id 1->n,name,balance
# withdraw,deposite
from abc import abstractmethod
class BankAcc:
    count=1
    def __init__(self,name,balance):
        self.id=BankAcc.count
        self.name=name
        self.balance=balance
        BankAcc.count=BankAcc.count+1
    def __str__(self):
        return f"id:{self.id},name:{self.name},balance:{self.balance}"
    def __gt__(self,acc):
        if isinstance(acc,BankAcc):
            return self.balance > acc.balance
        else:
            raise TypeError("unspported datatype")
    def withdraw(self,amount):
        if amount <=self.balance:
            self.balance=self.balance-amount
            print("amount:",amount,"new balanc",self.balance)
        else:
            print("your balance is not enough")
    def deposite(self,amount):
            self.balance=self.balance+amount
            print("amount:",amount,"new balanc",self.balance)
    @abstractmethod
    def type(self):
        pass
# id 1->n,name,balance,hr_salary_acc
# withdraw,deposite        
class VIP(BankAcc):
    def __init__(self,name,balance,hsa):
        super().__init__(name,balance)
        self.hsa=hsa
    def __str__(self):
       return super().__str__()+f",hsa:{self.hsa}" 
    def withdraw(self, amount):
        return super().withdraw(1.1*amount) 
    @abstractmethod
    def type(self):
        print("vip account")  
        