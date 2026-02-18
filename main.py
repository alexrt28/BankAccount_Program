from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

checking1 = CheckingAccount("Johnathon", 5000, 500, 400)
checking2 = CheckingAccount("Miriam", 12000, 1000, 5000)

savings1 = SavingsAccount("Emilia", 20000, 3000, 0.05)
savings2 = SavingsAccount("Walton", 16000, 1000, 0.04)

print(" ==== Assignment Scenario below: ===")
checking1.deposit(500)
checking1.withdraw(100)
checking1.transfer(500, savings2)   #will fail because $500 > $400 transfer limit
print(" === End Assignment Scenario. ===")
