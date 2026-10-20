from library import Library
from store import Store

class User:
    def __init__(self, username: str, wallet: float):
        self.username = username
        self.wallet = wallet
        self.library = Library()  # The library is created by the user (composition)

    def purchase_product(self, product):
        # Accesses the Singleton Store to make sure it's valid/exists in the catalogue
        store = Store()

        if product not in store.catalogue:
            print("Product not found in the store!")
            return False

        # 2. Check if the user has enough money in their wallet
        if self.wallet >= product.price:
            # 3. Deduct the funds
            self.wallet -= product.price

            # 4. Add the product to the user's personal Library collection
            self.library.collection.append(product)
            print(f"{self.username} successfully bought {product.title}!")
            return True
        else:
            print("Insufficient funds in wallet!")
            return False