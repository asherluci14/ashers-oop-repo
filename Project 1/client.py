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