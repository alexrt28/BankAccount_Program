from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount


checking1 = CheckingAccount("Johnathon", 5000, 500, 1234, 8880, 400)
checking2 = CheckingAccount("Miriam", 12000, 1000, 1235, 8889, 5000)

savings1 = SavingsAccount("Emilia", 20000, 3000, 1236, 8881,0.05)
savings2 = SavingsAccount("Walton", 16000, 1000, 1237, 8898, 0.04)

print("")
print("==== Assignment Scenarios below: ===")
checking1.deposit(500)
checking1.withdraw(100)
checking1.transfer(500, savings2)   #will fail because $500 > $400 transfer limit
checking1.transfer(350, savings2)   #will succeed, transfer under $400
savings1.apply_interest()
savings2.apply_interest()
print("=== End Assignment Scenarios. ===")
