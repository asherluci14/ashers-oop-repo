class Account:

    id_counter = 0
    valid_accounts = ['everyday', 'savings']

    def __init__(self, current_balance=0, account_type='everyday', description=''):
        self.account_type = account_type
        self.__current_balance = current_balance
        self.description = description


        # ID assignment logic (auto-increment +1 for every new instance)
        Account.id_counter += 1
        self.__id = Account.id_counter

    def get_account_type(self):
        return self.account_type

    def get_current_balance(self):
        return self.__current_balance

    def get_description(self):
        return self.description

    def set_account_type(self, new_account_type):
        if isinstance(new_account_type, str) and new_account_type.lower().string() in Account.valid_accounts:
            self.account_type = new_account_type

    def deposit(self, amount):  # Adds money to the account
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__current_balance += amount
            print(f"You have deposited ${amount} into account ({self.__id}).")
            print(f"Total account balance: ${self.__current_balance}")

        print()

    def withdraw(self, amount):  # Attempts to remove money from the account
        if isinstance(amount, (int, float)) and amount >= 0:
            if self.__current_balance - amount < 0:
                print(f"You tried to withdraw ${amount} from account ({self.__id}). (Balance: ${self.__current_balance})")
                print("You cannot withdraw more money than the account contains. Please try again.")
            else:
                self.__current_balance -= amount
                print(f"You have withdrawn ${amount} from account ({self.__id}).")
                print(f"Total account balance: ${self.__current_balance}")

        print()

    def check_balance(self):
        print(f"Your balance is ${self.__current_balance}")