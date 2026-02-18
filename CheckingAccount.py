from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self,customer_name, current_balance, minimum_balance, transfer_limit):
        super().__init__(customer_name,current_balance,minimum_balance)
        self.transfer_limit = transfer_limit

    def transfer(self, amount, destination_account):
        if amount > self.transfer_limit:
            print(f"Transfer failed: Transfer amount exceeds transfer limit of ${self.transfer_limit}")
        else:
            self.withdraw(amount)
            destination_account.deposit(amount)
            print(f"${amount} transferred successfully.")
