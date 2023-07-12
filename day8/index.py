from banke import *
def bigger(acc1,acc2):
    if acc1.balance>acc2.balance:
        return acc1
    elif acc2.balance>acc1.balance:
        return acc2
    else:
        return 0
acc_1=BankAcc("monda",7000)
acc_2=BankAcc("amira",7000)
print(acc_1,acc_2)  
acc_1.deposite(3000)
acc_1.withdraw(2000)
print(acc_2>acc_1) 
# acc_2>acc_1-->isbiger
#oprator overloading
#  4+5
#  "amira"+"MOHAMED"  
vip_1=VIP("elon",8000000,200000)
print(vip_1)
vip_1.withdraw(5000)
vip_1.type()
