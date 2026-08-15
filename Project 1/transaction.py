class Transaction:

    transaction_num = 0
    # Doesn't include "pending" because it should never go back to pending
    valid_statuses = ['cancelled', 'processed']

    def __init__(self, amount, type, description='', status="pending"):
        self.amount = amount
        self.type = type
        self.description = description
        self.status = status

        # Auto-increments the transaction number by 1 for each instance of a transaction (unique transaction ID)
        Transaction.transaction_num += 1
        self.id = Transaction.transaction_num

    def __str__(self):
        return (f"Transaction {self.get_id()}. A {self.get_type()} for ${self.get_amount()}. "
                f"Currently {self.get_status()}. Description: {self.get_description}")

    def __repr__(self):
        return f"Transaction(id={self.get_id()}, {self.get_amount()}, {self.get_type()}, {self.get_status()})"

    def get_amount(self):
        return self.amount

    def get_status(self):
        return self.status

    def get_id(self):
        return self.id

    def get_type(self):
        return self.type

    def get_description(self):
        return self.description

    def change_status(self, new_status):
        if self.status in Transaction.valid_statuses:
            print(
                f"The transaction status has already been set to \"{self.status}\" can cannot be undone.")
        else:
            if new_status.lower().strip() in Transaction.valid_statuses:
                self.status = new_status

                print(f"Transaction ({self.id}) was {self.status}.")

    def process_transaction(self):
        self.change_status('processed')

    def cancel_transaction(self):
        self.change_status('cancelled')
