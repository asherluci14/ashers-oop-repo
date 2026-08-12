class Client:

    id_counter = 0  # Used for assigning IDs to new clients
    valid_contacts = ['phone', 'email']

    def __init__(self, name, phone, email, address, preferred_contact='email'):
        self.name = name
        self.__phone = phone
        self.__email = email
        self.__address = address
        self.preferred_contact = preferred_contact

        # ID assignment logic (auto-increment +1 for every new instance)
        Client.id_counter += 1
        self.__id = Client.id_counter

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_id(self):
        return self.__id

    def get_preferred_contact(self):
        return self.preferred_contact

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.name = new_name

    def set_phone(self, new_phone):
        if isinstance(new_phone, (str, int)):
            self.__phone = new_phone

    def set_email(self, new_email):
        if isinstance(new_email, str):
            self.__email = new_email

    def set_address(self, new_address):
        if isinstance(new_address, str):
            self.__email = new_address

    def set_preferred_contact(self, new_contact):
        if isinstance(new_contact, str) and new_contact.lower().strip() in Client.valid_contacts:
            self.preferred_contact = new_contact


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


client_1 = Client(
    name="John Doe",
    phone="+1-555-0101",
    email="john.doe@example.com",
    address="123 Main Street, Springfield, IL 62701",
    preferred_contact="email"
)

client_2 = Client(
    name="Jane Smith",
    phone="+1-555-0102",
    email="jane.smith@example.com",
    address="456 Oak Avenue, Metropolis, NY 10001",
    preferred_contact="phone"
)

client_3 = Client(
    name="Alex Jones",
    phone="+1-555-0103",
    email="alex.jones@example.com",
    address="789 Pine Road, Riverdale, CA 90210",
    preferred_contact="email"
)

account_1 = Account(100, 'savings', 'For savings.')
account_2 = Account(20)
account_3 = Account(1738)

client_1.get_name()
client_2.get_email()
client_2.get_id()
client_3.get_id()

account_1.deposit(20)
account_3.deposit(999)
account_2.withdraw(40)
account_2.withdraw(5)
account_3.withdraw(50)

