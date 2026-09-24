from account import Account

class SavingsAccount(Account):
    """
        Intended to represent a savings account with minimum balance enforcement and interest tracking

        Attributes:
            MIN_BALANCE (int): The minimum balance required to maintain in the account (200)
            interest_rate (int): The annual interest rate applied to the account
            Inherits all other attributes from Account

        Methods:
            withdraw(amount): Withdraws funds ensuring the minimum balance threshold is preserved
            get_interest_rate(): Returns the current interest rate value
            Inherits all other methods from Account
    """

    MIN_BALANCE = 200

    def __init__(self, current_balance, description, interest_rate):
        super().__init__(account_type="savings", current_balance=current_balance, description=description)
        self.__interest_rate = interest_rate

    def get_interest_rate(self):
        return self.__interest_rate

    def withdraw(self, amount):

        # Validates that the resulting value in the savings account will stay above the minimum allowed balance
        if isinstance(amount, (int, float)):
            if (self.current_balance - amount) < self.MIN_BALANCE:
                print(f"Account {self.id} (balance: {self.current_balance}) tried to withdraw ${amount}.")
                print(f"You cannot go below the minimum balance. Withdrawal failed.")
                return False

            else:

                # Standard withdrawal behaviour
                if amount >= 0:
                    if self._current_balance - amount < 0:
                        print(f"You tried to withdraw ${amount} from account ({self.id}). "
                              f"(Balance: ${self.current_balance})")
                        print("You cannot withdraw more money than the account contains. Please try again.")
                        return False
                    else:
                        self._current_balance -= amount
                        print(f"You have withdrawn ${amount} from account ({self.id}).")
                        print(f"Updated account balance: ${self.current_balance}")

                        self.create_transaction(amount, "withdraw", self.current_balance)

                        print()  # Just used for formatting a blank line

                        return True

                else:
                    return False

        else:
            print("Entered withdrawal amount must be a number.")
            return False

    interest_rate = property(get_interest_rate)
