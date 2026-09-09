from account import Account

class SavingsAccount(Account):

    MIN_BALANCE = 0  # Should this be changed later?

    def __init__(self, current_balance, description, interest_rate):
        super().__init__(account_type="savings", current_balance=current_balance, description=description)
        self.__interest_rate = interest_rate

    def get_interest_rate(self):
        return self.__interest_rate

    def withdraw(self, amount):

        if isinstance(amount, (int, float)):
            if (self.current_balance - amount) < self.MIN_BALANCE:
                print(f"Account {self.id} tried to withdraw ${amount}.")
                print(f"Account {self.id} only has ${self.current_balance}. Withdrawal was not processed.")
            else:
                super().withdraw(amount)
        else:
            print("Entered withdrawal amount must be a number.")

    interest_rate = property(get_interest_rate)
