class BankAccount:
    #class attribute
    bank_title = "Platinum Shield Bank"

    #instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    #deposit method
    def deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            print(f"Deposited ${amount}. New balance: {self.current_balance}")
        else:
            print(f"Deposit amount must be greater than 0")

    #withdraw method
    def withdraw(self, amount):
        if amount <= 0:
            print(f"Withdraw amount must be greater than 0")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"Withdrawal denied. Balance cannot go less than ${self.minimum_balance}")
        else:
            self.current_balance -= amount
            print(f"Withdrawal successful. New balance: ${self.current_balance}")

    def print_customer_information(self):
        print("----- Customer Information -----")
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")
        print("--------------------------------")


account1 = BankAccount("Jim John", 1000, 100)
account2 = BankAccount("Sarah Madison", 5000, 500)

# Print customer information
account1.print_customer_information()
account2.print_customer_information()

# Testing deposit method
account1.deposit(500)
account2.deposit(1000)

# Testing withdraw method with valid withdrawal
account1.withdraw(200)
account2.withdraw(2000)

# Testing withdraw method with validation
account1.withdraw(1500)
account2.withdraw(3600)
