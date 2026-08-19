class Transaction:

    __transaction_num = 0
    # Doesn't include "pending" because it should never go back to pending
    __valid_statuses = ['cancelled', 'processed']

    def __init__(self, amount, type, description='', status="pending"):
        # Auto-increments the transaction number by 1 for each instance of a transaction (unique transaction ID)
        Transaction.__transaction_num += 1
        self.__id = Transaction.__transaction_num

        if isinstance(amount, (int,float)):
            self.__amount = amount
        else:
            print("Amount must be an integer or a float number.")
            self.__amount = 0  # TODO: This is bad design, an error should be raised instead
            print("Amount has been set to 0.")

        if isinstance(type, str):
            self.__type = type
        else:
            print("Type must be a string.")
            self.__type = ""
            print("Type has been set to an empty string.")

        if isinstance(description, str):
            self.__description = description
        else:
            print("Description must be a string.")
            self.__description = ""
            print("Description has been set to an empty string.")

        if (status.lower().strip() in Transaction.__valid_statuses) or (status.lower().strip() == "pending"):
            self.__status = status
        else:
            print("Status can only be set to \"pending\", \"cancelled\", or \"processed\".")
            self.__preferred_contact = "pending"
            print("Status has been set to \"pending\".")

    def __str__(self):
        return (f"Transaction {self.get_id()}. A {self.get_type()} for ${self.get_amount()}. "
                f"Currently {self.get_status()}. Description: {self.get_description}")

    def __repr__(self):
        return f"Transaction(id={self.get_id()}, {self.get_amount()}, {self.get_type()}, {self.get_status()})"

    def get_amount(self):
        return self.__amount

    def get_status(self):
        return self.__status

    def get_id(self):
        return self.__id

    def get_type(self):
        return self.__type

    def get_description(self):
        return self.__description

    def set_description(self, new_desc):
        if isinstance(new_desc, str):
            self.__description = new_desc
        else:
            print("New description must be a string.")

    def change_status(self, new_status):
        if self.__status in Transaction.__valid_statuses:
            print(
                f"The transaction status has already been set to \"{self.__status}\" can cannot be undone.")
        else:
            if new_status.lower().strip() in Transaction.__valid_statuses:
                self.__status = new_status

                print(f"Transaction ({self.__id}) was {self.__status}.")

    def process_transaction(self):
        self.change_status('processed')

    def cancel_transaction(self):
        self.change_status('cancelled')
