from library import Library
from store import Store

class User:

    def __init__(self, username: str, wallet: float):
        self.username = username
        self.wallet = wallet
        self.library = Library()  # The library is created by the user (composition)

    def purchase_product(self, product) -> bool:

        # Accesses the Singleton Store to make sure it's valid/exists in the catalogue
        store = Store()

        # Checks if the product is available and isn't delisted
        if product not in store.catalogue:
            print("This product is not available for purchase (it may be delisted or non-existent).")
            return False

        # Checks if the user has enough money in their wallet
        if self.wallet >= product.price:
            # Deducts the funds
            self.wallet -= product.price

            # Adds the product to the user's personal Library collection
            self.library.collection.append(product)
            print(f"{self.username} successfully bought {product.title}!")
            return True

        else:
            print("Insufficient funds in wallet!")
            return False