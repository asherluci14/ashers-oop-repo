# This class represents one branch of the organisation

class Branch:
    def __init__(self, number, name, location, phone, is_open=False):
        self.number = number
        self.name = name
        self.location = location
        self.phone = phone
        self.is_open = is_open

    def __str__(self):
        open_text = "open" if self.is_open else "not open"
        return f"Branch {self.number} ({self.name} branch) at {self.location}. Currently {open_text}. PH: {self.phone}"

    def __repr__(self):
        return f"Branch({self.number}, {self.name}, {self.location}, {self.phone}, {self.is_open})"

    def set_phone(self, new_phone):
        if isinstance(new_phone, (int, str)):  # Potentially add some proper phone number checking here (char lim)
            self.phone = new_phone

    def change_status(self, new_status):
        if isinstance(new_status, bool):
            self.is_open = new_status

            status = 'open' if new_status else 'closed'

            print(f"Branch {self.number} is now {status}.")

    def open_branch(self):
        if self.is_open:
            print(f"Branch {self.number} is already open.")
        else:
            self.change_status(True)

    def close_branch(self):
        if not self.is_open:
            print(f"Branch {self.number} is already closed.")
        else:
            self.change_status(False)

    def change_phone(self, new_phone):
        self.set_phone(new_phone)
        print(f"Branch {self.number}'s phone number has been set to {self.phone}.")