from account import Account

class EverydayAccount(Account):
    """
        Intended to represent an everyday checking account with single-withdrawal limits

        Attributes:
            MAX_WITHDRAW (int): The maximum allowable amount for a single withdrawal (1000)
            Inherits all other attributes from Account

        Methods:
            withdraw(amount): Withdraws funds ensuring the single transaction maximum limit is respected
            Inherits all other methods from Account
    """

    MAX_WITHDRAW = 1000

    def __init__(self, current_balance, description):
        super().__init__(account_type="everyday", current_balance=current_balance, description=description)

    # Removes money from the account
    def withdraw(self, amount):

        # Validates that the withdrawal amount is under the maximum allowed withdrawal amount
        if isinstance(amount, (int, float)):
            if amount > self.MAX_WITHDRAW:
                print(f"The maximum you can withdraw is ${self.MAX_WITHDRAW}. Please try again.")
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
