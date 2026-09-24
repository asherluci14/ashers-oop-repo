class Branch:
    """
        Intended to manage bank branch details and operational status

        Attributes:
            branch_counter (int): Counter used to track or generate branch IDs
            name (str): The name of the bank branch
            location (str): The physical location or address of the branch
            phone (int, str): The contact phone number for the branch
            is_open (bool): The operational status indicating if the branch is currently open

        Methods:
            get_number(): Returns the branch identifier number
            get_name(): Returns the name of the branch
            get_location(): Returns the location string of the branch
            get_phone(): Returns the phone number of the branch
            get_is_open(): Returns True if the branch is open, otherwise False
            set_location(): Updates the physical location of the branch
            set_phone(): Updates the phone number of the branch
            change_status(new_status): Updates the open or closed status of the branch
            open_branch(): Opens the branch for business operations
            close_branch(): Closes the branch operations
            change_phone(): Modifies or updates the contact phone details
    """

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
        return f"Branch(number={self.__number}, {self.__name}, {self.__location}, {self.__phone}, {self.__is_open})"

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
            return False
        else:
            self.change_status(True)
            return True

    def close_branch(self):
        if not self.__is_open:
            print(f"Branch {self.__number} is already closed.")
            return False
        else:
            self.change_status(False)
            return True

    def change_phone(self, new_phone):
        self.set_phone(new_phone)
        print(f"Branch {self.__number}'s phone number has been set to {self.__phone}.")

    number = property(get_number)
    name = property(get_name)
    location = property(get_location, set_location)
    phone = property(get_phone, set_phone)
    is_open = property(get_is_open)