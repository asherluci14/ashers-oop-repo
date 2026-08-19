from client import Client
from account import Account
from branch import Branch
from transaction import Transaction

# ----------------------------- Object Instantiation --------------------------------


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

transaction_1 = Transaction(20, 'deposit')
transaction_2 = Transaction(30, 'withdraw')
transaction_3 = Transaction(50, 'deposit')

branch_1 = Branch('location1', '5000', '0411111111')
branch_2 = Branch('location2', '5001', '0422222222')
branch_3 = Branch('location3', '5002', '0433333333')


# -------------------------------------------------------------

print(client_1)
print(repr(client_1))

client_1.set_phone('0412345678')
account_1.deposit(300)
account_2.withdraw(300)
transaction_1.process_transaction()
transaction_2.cancel_transaction()
transaction_2.process_transaction()
branch_1.open_branch()
branch_2.open_branch()
branch_3.close_branch()
branch_2.change_phone('0412345678')

print(branch_1)
print(repr(branch_1))

print(client_1)
print(repr(client_1))  # phone number was changed

print(account_1)
print(repr(account_1))

print(transaction_1)
print(repr(transaction_1))

# ------------- Client-Account Aggregation Testing ---------------

client_1.add_account(account_1)
client_1.add_account(account_3)
client_2.add_account(account_2)
print(client_1.get_account_list())
client_1.remove_account(account_1)
print(client_1.get_account_list())

print(account_1.get_current_balance())


# ------------ Client-Branch Association Testing ------------
client_1.set_preferred_branch(branch_1)
print(client_1.get_preferred_branch())
client_1.set_preferred_branch(branch_2)
print(client_1.get_preferred_branch())
client_1.clear_preferred_branch()
print(client_1.get_preferred_branch())