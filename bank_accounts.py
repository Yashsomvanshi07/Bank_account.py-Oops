class BalanceException(Exception):
    pass
    

class BankAccount :
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}'created.\nBalance = ₹{self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' Balance = ₹{self.balance:.2f}")
        
        
    def deposite(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposite complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, Account'{self.name}' only has a balance of ₹{self.balance:.2f}"
            )
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')    
                      
                      
    def transfer(self, amount, account):
        try:
            print('\n***************\n\nBeginning Transfer...🐱‍🏍')
            self.viableTransaction(amount)
            account.deposite(amount)
            print('\nTransfer complete!🤩 ✔\n\n***************')
        except BalanceException as error:
            print(f'\nTransfer interrupted. ❌ {error} ')    
            
            
class InterestRewardAcct(BankAccount):
    def deposite(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposite complete.")
        self.getBalance()
                 
class SavingsAcct(InterestRewardAcct):
    def __init__(self, initialAmount, acctName):
        # Correct way to call the parent class's constructor
        super().__init__(initialAmount, acctName)
        self.fee = 5

    def withdraw(self, amount):
        try:
            # Ensure the transaction is viable (including the fee)
            self.viableTransaction(amount + self.fee)
            # Deduct the withdrawal amount and fee from balance
            self.balance -= (amount + self.fee)
            print("\nWithdraw completed.")
            # Display the updated balance
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

                       
                                      