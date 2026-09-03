"""
This class represents an account that belongs to a client.
It's responsible for managing the account's financial information,
and it provides methods for depositing/withdrawing money and checking
the current balance.
"""

from transaction import Transaction

class Account:

    __id_counter = 0
    __valid_accounts = ['everyday', 'savings']

    def __init__(self, current_balance=0, account_type='everyday', description=''):

        # ID assignment logic (auto-increment +1 for every new instance)
        Account.__id_counter += 1
        self.__id = Account.__id_counter

        # TODO: implement proper error raising instead of setting default values

        if isinstance(current_balance, (int, float)):
            self.__current_balance = current_balance
        else:
            print("Current balance must be an integer or a float number.")
            self.__current_balance = 0
            print("Current balance has been set to 0.")

        if isinstance(account_type, str) and account_type.lower().strip() in Account.__valid_accounts:
            self.__account_type = account_type
        else:
            print("Account type must be \"everyday\" or \"savings\".")
            self.__account_type = "savings"
            print("Account type has been set to \"savings\".")

        if isinstance(description, str):
            self.__description = description
        else:
            print("Description must be a string.")
            self.__description = ""
            print("Description has been set to an empty string.")

        self.__transactions = []

    def __str__(self):
        return (f"{self.account_type.capitalize()} account (id: {self.id}) "
                f"has ${self.current_balance}.")

    def __repr__(self):
        return f"Account(id={self.id}, {self.current_balance}, {self.account_type})"

    def get_account_type(self):
        return self.__account_type

    def get_current_balance(self):
        return self.__current_balance

    def get_description(self):
        return self.__description

    def get_id(self):
        return self.__id

    def get_transactions(self):
        return self.__transactions

    def set_account_type(self, new_account_type):
        if isinstance(new_account_type, str) and new_account_type.lower().strip() in Account.__valid_accounts:
            self.__account_type = new_account_type
        else:
            print("Account type must be \"everyday\" or \"savings\".")

    def set_description(self, new_desc):
        if isinstance(new_desc, str):
            self.__description = new_desc
        else:
            print("New description must be a string.")

    def deposit(self, amount):  # Adds money to the account
        if isinstance(amount, (int, float)) and amount >= 0:
            self.__current_balance += amount
            print(f"You have deposited ${amount} into account ({self.__id}).")
            print(f"Updated account balance: ${self.current_balance}")

            self.create_transaction(amount, "deposit", self.current_balance)

        print()

    def withdraw(self, amount):  # Attempts to remove money from the account
        if isinstance(amount, (int, float)) and amount >= 0:
            if self.__current_balance - amount < 0:
                print(
                    f"You tried to withdraw ${amount} from account ({self.id}). (Balance: ${self.current_balance})")
                print(
                    "You cannot withdraw more money than the account contains. Please try again.")
            else:
                self.__current_balance -= amount
                print(
                    f"You have withdrawn ${amount} from account ({self.id}).")
                print(f"Updated account balance: ${self.current_balance}")

                self.create_transaction(amount, "withdraw", self.current_balance)

        print()

    def check_balance(self):
        print(f"Your balance is ${self.current_balance}.")

    def create_transaction(self, amount, type, new_balance):
        self.transactions.append(Transaction(amount=amount,
                                             type=str(type),
                                             description=f'Resulting balance: {new_balance}',
                                             status="processed"))

    id = property(get_id)
    current_balance = property(get_current_balance)
    account_type = property(get_account_type, set_account_type)
    description = property(get_description, set_description)
    transactions = property(get_transactions)