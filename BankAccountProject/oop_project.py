from BankAccount import *

Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

Dave.deposit(3000)

Dave.withdraw(10000)
Dave.withdraw(10)

Dave.transfer(500, Sara)

Jim = InterestRewardsAccount(1000, "Jim")

Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Dave)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(1000, Sara)