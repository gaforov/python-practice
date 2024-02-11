from bank_accounts import *

Said = BankAccount(1000, "Said")
John = BankAccount(2000, "John")

Said.getBalance()
# John.getBalance()

Said.deposit(500)
# John.deposit(200)

Said.withdraw(200)
Said.withdraw(2000)

print("\n------------------ 1\n")

Said.transfer(1000, John)
Said.transfer(2000, John)
Said.transfer(200, John)

print("\n------------------ 2\n")

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Said) #Said account had $100 up to this point, should be $200 after this line

print("\n------------------ 3\n")

Mary = SavingsAccount(1000, "Mary")
Mary.getBalance()
Mary.deposit(100)
Mary.transfer(10000,Said)
Mary.transfer(200, Said) #Said account had $200 up to this point, should be $400 after this line ($5 fee gets deducted too = $205)

