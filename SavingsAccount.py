import BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, interest_rate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"Interest applied: ${interest:.2f}")
        print(f"New balance: ${self.current_balance:.2f}")