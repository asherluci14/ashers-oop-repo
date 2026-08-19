# This class represents one branch of the organisation

class Branch:

    __branch_counter = 0

    def __init__(self, name, location, phone, is_open=False):
        Branch.__branch_counter += 1
        self.__number = Branch.__branch_counter

        if isinstance(name, str):
            self.__name = name
        else:
            print("Branch name must be a string.")
            self.__name = f"Branch {self.__number}"
            print(f"Branch name has been set to \"{self.__name}\".")

        if isinstance(location, str):
            self.__location = location
        else:
            print("Branch location must be a string.")
            self.__location = ""
            print(f"Branch location has been set to an empty string.")

        if isinstance(phone, (int, str)):
            self.__phone = phone
        else:
            print("Supplied phone number must be a string or an integer.")
            self.__phone = ""
            print(f"Phone number has been set to an empty string.")

        if isinstance(is_open, bool):
            self.__is_open = is_open
        else:
            print("Open/close status must be a boolean value.")
            self.__is_open = False
            print(f"Branch {self.__number} has been set to \"closed\".")

    def __str__(self):
        open_text = "open" if self.__is_open else "not open"
        return f"Branch {self.__number} ({self.__name} branch) at {self.__location}. Currently {open_text}. PH: {self.__phone}"

    def __repr__(self):
        return f"Branch({self.__number}, {self.__name}, {self.__location}, {self.__phone}, {self.__is_open})"

    def get_number(self):
        return self.__number

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_phone(self):
        return self.__phone

    def get_is_open(self):
        return self.__is_open

    def set_location(self, new_location):
        if isinstance(new_location, str):
            self.__location = new_location
        else:
            print("New location must be in a string format.")

    def set_phone(self, new_phone):
        if isinstance(new_phone, (int, str)):  # Potentially add some proper phone number checking here (char lim)
            self.__phone = new_phone
        else:
            print("Supplied phone number must be a string or an integer.")

    def change_status(self, new_status):
        if isinstance(new_status, bool):
            self.__is_open = new_status

            status = 'open' if new_status else 'closed'

            print(f"Branch {self.__number} is now {status}.")

    def open_branch(self):
        if self.__is_open:
            print(f"Branch {self.__number} is already open.")
        else:
            self.change_status(True)

    def close_branch(self):
        if not self.__is_open:
            print(f"Branch {self.__number} is already closed.")
        else:
            self.change_status(False)

    def change_phone(self, new_phone):
        self.set_phone(new_phone)
        print(f"Branch {self.__number}'s phone number has been set to {self.__phone}.")