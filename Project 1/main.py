from client import Client
from branch import Branch
from savings_account import SavingsAccount
from everyday_account import EverydayAccount
from account import Account
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

account_1 = SavingsAccount(100, 'savings', 3.5)
account_2 = SavingsAccount(20, "", 3)
account_3 = EverydayAccount(1738, "Everyday acc")

branch_1 = Branch('location1', '5000', '0411111111')
branch_2 = Branch('location2', '5001', '0422222222')
branch_3 = Branch('location3', '5002', '0433333333')


# -------------------------------------------------------------

print(client_1)
print(repr(client_1))

client_1.phone = "0412345678"
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

# ------------- Client-Account Aggregation Testing ---------------

client_1.add_account(account_1)
client_1.add_account(account_3)
client_2.add_account(account_2)
print(client_1.account_list)
client_1.remove_account(account_1)
print(client_1.account_list)

print(account_1.current_balance)


# ------------ Client-Branch Association Testing ------------
client_1.preferred_branch = branch_1
print(client_1.preferred_branch)
client_1.preferred_branch = branch_2
print(client_1.preferred_branch)
client_1.clear_preferred_branch()
print(client_1.preferred_branch)


# ------------ Account - Transaction Composition Testing ------------

account_1.withdraw(300)
account_2.withdraw(300)

account_1.deposit(300)
account_2.deposit(1000)
account_3.deposit(13570)
account_2.deposit(1000)
account_2.withdraw(3000)
account_2.withdraw(500)

print(account_1.transactions)
print(account_2.transactions)
print(account_3.transactions)

print(isinstance(account_1, Account))
print(isinstance(account_3, Account))
print(account_1)
print(account_3)
