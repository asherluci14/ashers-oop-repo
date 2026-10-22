from product import Product

class Library:

    def __init__(self):

        self.__collection = []  # The user's collection of Product objects will be stored in here

    def __str__(self):
        return f"A library of items purchased from the store, containing {len(self.__collection)} products."

    def get_collection(self):
        return self.__collection

    collection = property(get_collection)

    def add_product(self, product: Product):
        """Adds a purchased product to the user's library."""

        # Type checking
        if not isinstance(product, Product):
            raise TypeError("Library can only contain valid Product objects.")

        if product not in self.__collection:
            self.__collection.append(product)

    def remove_product(self, product: Product):
        """Removes a product from the library."""

        # Type checking
        if not isinstance(product, Product):
            raise TypeError("Product parameter must be a Product object.")

        if product in self.__collection:
            self.__collection.remove(product)

    def has_product(self, product: Product) -> bool:

        # Type checking
        if not isinstance(product, Product):
            raise TypeError("Product parameter must be a Product object.")

        # Returns True if the collection contains the product, returns False if vice versa

        if product in self.__collection:
            return True

        else:
            return False