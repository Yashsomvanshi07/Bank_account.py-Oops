from bank_accounts import *

Yash = BankAccount(10000, "Yash")
Mahesh = BankAccount(30000, "Mahesh")


Yash.getBalance()
Mahesh.getBalance()


Yash.deposite(1399)


Yash.withdraw(40000)
Yash.withdraw(40)

Yash.transfer(40000, Mahesh)
Yash.getBalance()

Rohit = InterestRewardAcct(1000, "Rohit")
Rohit.getBalance()
Rohit.deposite(100)
Rohit.transfer(100, Yash)


Rohit.getBalance()
Yash.transfer(95, Rohit)

Mohan = SavingsAcct(3000, "Mohan")
Mohan.getBalance()
Mohan.deposite(3000)
Mohan.transfer(300, Yash)