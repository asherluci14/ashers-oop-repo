from client import Client
from account import Account

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

print(client_1.get_name())
print(client_2.get_email())
print(client_2.get_id())
print(client_3.get_id())

account_1.deposit(20)
account_3.deposit(999)
account_2.withdraw(40)
account_2.withdraw(5)
account_3.withdraw(50)

