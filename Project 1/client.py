from account import Account
from branch import Branch

class Client:
    """
        Intended to represent a bank client who manages accounts and preferred branch settings

        Attributes:
            id_counter (int): Counter used to generate unique client IDs
            valid_contacts (list[str]): List of valid contact method types allowed
            id (int): Unique identifier for the client
            name (str): The full name of the client
            phone (int, str): The contact phone number of the client
            email (str): The email address of the client
            address (str): The residential address of the client
            preferred_contact (str): The client's preferred mode of communication
            account_list (list[Account]): List of account objects owned by the client
            preferred_branch (str): The client's preferred bank branch

        Methods:
            get_name(): Returns the name of the client
            get_phone(): Returns the phone number of the client
            get_email(): Returns the email address of the client
            get_address(): Returns the address of the client
            get_id(): Returns the client's unique ID
            get_preferred_contact(): Returns the preferred contact method string
            get_account_list(): Returns the list of accounts owned by the client
            get_preferred_branch(): Returns the preferred branch object or string
            set_name(): Updates the name of the client
            set_phone(): Updates the phone number of the client
            set_email(): Updates the email address of the client
            set_address(): Updates the residential address
            set_preferred_contact(): Updates the preferred contact method
            set_preferred_branch(): Sets the preferred bank branch
            clear_preferred_branch(): Removes the current preferred branch assignment
            clear_account_list(): Clears all accounts associated with the client
            add_account(account): Adds a new account object to the client's account list
            remove_account(account): Removes a specific account from the client's account list
    """
    __id_counter = 0  # Used for assigning IDs to new clients
    __valid_contacts = ['phone', 'email']

    def __init__(self, name, phone, email, address, preferred_contact='email'):
        # ID assignment logic (auto-increment +1 for every new instance)
        Client.__id_counter += 1
        self.__id = Client.__id_counter

        if isinstance(name, str):
            self.__name = name
        else:
            print("Name must be a string.")
            self.__name = ""
            print("Name has been set to an empty string.")

        if isinstance(phone, (int, str)):
            self.__phone = phone
        else:
            print("Supplied phone number must be a string or an integer.")
            self.__phone = ""
            print(f"Phone number has been set to an empty string.")

        if isinstance(email, str):
            self.__email = email
        else:
            print("Email must be a string.")
            self.__email = ""
            print("Email has been set to an empty string.")

        if isinstance(address, str):
            self.__address = address
        else:
            print("Address must be a string.")
            self.__address = ""
            print("Address has been set to an empty string.")

        if isinstance(preferred_contact, str) and preferred_contact.lower().strip() in Client.__valid_contacts:
            self.__preferred_contact = preferred_contact
        else:
            print("Preferred contact can only be either \"phone\" or \"email\".")
            self.__preferred_contact = "email"
            print("Preferred contact has been set to \"email\".")

        self.__account_list = []  # Clients can have multiple accounts

        self.__preferred_branch = ""

    def __str__(self):
        return f"This is client {self.id}, {self.name}. Prefers contact via {self.preferred_contact}."

    def __repr__(self):
        return (f"Client({self.name}, {self.phone}, {self.email}, {self.address}, "
                f"{self.__preferred_contact})")

    def get_name(self):
        return self.__name

    def get_phone(self):
        return self.__phone

    def get_email(self):
        return self.__email

    def get_address(self):
        return self.__address

    def get_id(self):
        return self.__id

    def get_preferred_contact(self):
        return self.__preferred_contact

    def get_account_list(self):
        return self.__account_list

    def get_preferred_branch(self):
        return self.__preferred_branch

    def set_name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("New name must be a string.")

    def set_phone(self, new_phone):
        if isinstance(new_phone, (str, int)):
            self.__phone = new_phone
        else:
            print("New phone number must be a string or an integer.")

    def set_email(self, new_email):
        if isinstance(new_email, str):
            self.__email = new_email
        else:
            print("New email must be a string.")

    def set_address(self, new_address):
        if isinstance(new_address, str):
            self.__address = new_address
        else:
            print("New address must be a string.")

    def set_preferred_contact(self, new_contact):
        if isinstance(new_contact, str) and new_contact.lower().strip() in Client.__valid_contacts:
            self.__preferred_contact = new_contact
        else:
            print("Preferred contact can only be either \"phone\" or \"email\".")

    def set_preferred_branch(self, branch):
        if isinstance(branch, Branch) or branch == "":
            self.__preferred_branch = branch
        else:
            print("Preferred branch must be a Branch object!")

    def clear_preferred_branch(self):
        self.set_preferred_branch("")

    def clear_account_list(self):
        self.__account_list.clear()
        print("The account list has been cleared and is now empty.")

    def add_account(self, account):
        if account not in self.__account_list:
            if isinstance(account, Account):
                self.__account_list.append(account)
                return True
            else:
                print("New account must be an Account object.")
                return False
        else:
            print("This account already belongs to this client!")
            return False

    def remove_account(self, account):
        if account in self.__account_list:
            if isinstance(account, Account):
                self.__account_list.remove(account)
                return True
            else:
                print("You must provide an Account object.")
                return False
        else:
            print("This account does not belong to this client.")
            return False

    name = property(get_name, set_name)
    phone = property(get_phone, set_phone)
    email = property(get_email, set_email)
    address = property(get_address, set_address)
    preferred_contact = property(get_preferred_contact, set_preferred_contact)
    preferred_branch = property(get_preferred_branch, set_preferred_branch)
    account_list = property(get_account_list)
    id = property(get_id)