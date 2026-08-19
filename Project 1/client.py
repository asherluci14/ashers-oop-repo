class Client:

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

    def __str__(self):
        return f"This is client {self.get_id()}, {self.get_name()}. Prefers contact via {self.get_preferred_contact()}."

    def __repr__(self):
        return (f"Client({self.__name}, {self.get_phone()}, {self.get_email()}, {self.get_address()}, "
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
            self.__email = new_address
        else:
            print("New address must be a string.")

    def set_preferred_contact(self, new_contact):
        if isinstance(new_contact, str) and new_contact.lower().strip() in Client.__valid_contacts:
            self.__preferred_contact = new_contact
        else:
            print("Preferred contact can only be either \"phone\" or \"email\".")