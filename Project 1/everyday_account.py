from account import Account

class EverydayAccount(Account):

    MAX_WITHDRAW = 1000  # Max amount allowed to withdraw -- should this be changed later?

    def __init__(self, current_balance, description):
        super().__init__(account_type="everyday", current_balance=current_balance, description=description)


    def withdraw(self, amount):

        if isinstance(amount, (int, float)):
            if amount > self.MAX_WITHDRAW:
                print(f"The maximum you can withdraw is ${self.MAX_WITHDRAW}. Please try again.")
            else:
                super().withdraw(amount)
        else:
            print("Entered withdrawal amount must be a number.")