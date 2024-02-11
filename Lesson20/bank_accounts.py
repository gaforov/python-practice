class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(
            f"\nAccount '{self.name}' created. \nBalance: ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit of ${amount} is complete.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nReason: Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print(f"\nWithdraw amount of ${amount} is complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"❌ Withdraw interrupted ❌: {error}")

    def transfer(self, amount, account):
        try:
            print(
                f"\n* * * * * * * * * *\nBeginning Transfer of ${amount}.. 💰\n* * * * * * * * * *\n \nBalance before transfer:")
            self.getBalance()
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n* * * * * * * * * *\nTransfer complete ✅\n* * * * * * * * * *\n")
        except BalanceException as error:
            print(f"❌ Transfer interrupted ❌: {error}")


class InterestRewardsAcct(BankAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        print(
            f"\nInterest Rewards Account '{self.name}' created. \nBalance: ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount * 1.05
        print(f"\nDeposit of ${amount} is complete.")
        self.getBalance()


class SavingsAccount(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5

    # override existing withdraw method
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print(f"\nWithdraw amount of ${amount} is completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
