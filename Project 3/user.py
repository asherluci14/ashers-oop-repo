from library import Library
from store import Store
from dlc import DLC
from product import Product

class User:

    user_id = 0  # Used for assigning incrementing IDs to all User objects

    def __init__(self, username: str, wallet: int | float):

        # Type checking for all parameters
        if not isinstance(username, str):
            raise TypeError("Username parameter must be a string.")
        if not isinstance(wallet, (int, float)):
            raise TypeError("Wallet parameter is measured in dollars ($) and must be an integer or float number.")

        self.__username = username
        self.__wallet = wallet  # Measured in dollars ($), can be a float or integer
        self.__library = Library()  # The library is created by the user (composition)

        # Increments the user ID by 1 and assigns it to the private attribute "id"
        User.user_id += 1
        self.__id = User.user_id

    def get_username(self):
        return self.__username

    def get_wallet(self):
        return self.__wallet

    def get_library(self):
        return self.__library

    def get_id(self):
        return self.__id

    username = property(get_username)
    wallet = property(get_wallet)
    library = property(get_library)

    def add_funds(self, amount: int | float):

        if not isinstance(amount, (int, float)):
            raise TypeError(f"Amount parameter is measured in dollars ($) and must be an integer or float number.")

        self.__wallet += amount

    def purchase_product(self, product) -> bool:

        # Accesses the Singleton Store to make sure it's valid/exists in the catalogue
        store = Store()

        # Type checking
        if not isinstance(product, Product):
            print("Product parameter must be a Product object.")
            return False

        # Checks if the user already owns the Product
        if self.__library.has_product(product):
            print(f"{self.username} already owns the product \"{product.title}\".")
            return False

        # Checks if the product is available and isn't delisted
        if product not in store.catalogue:
            print("This product is not available for purchase (it may be delisted or non-existent).")
            return False

        # Verifies that the user owns the base game required for the DLC (if it's a DLC)
        if isinstance(product, DLC):
            if not self.__library.has_product(product.base_game):
                print(
                    f"Cannot purchase '{product.title}': You must own the base game '{product.base_game.title}' first!")
                return False

        # Checks if the user has enough money in their wallet
        if self.__wallet < product.price:
            print("Insufficient funds in wallet!")
            return False

        # Deducts the funds
        self.__wallet -= product.price

        # Adds the product to the user's personal Library collection
        self.__library.add_product(product)
        print(f"{self.username} successfully bought {product.title}!")
        return True
