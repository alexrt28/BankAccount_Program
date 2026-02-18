class BankAccount:
    #class attribute
    bank_title = "Platinum Shield Bank"

    #instance attributes
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        #protected member
        self.account_number = account_number
        #private member
        self.routing_number = routing_number

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
        print(f"Account Number: {self.account_number}")
        print(f"Routing Number: {self.routing_number}")
        print(f"Current Balance: ${self.current_balance}")
        print(f"Minimum Balance: ${self.minimum_balance}")
        print("--------------------------------")
