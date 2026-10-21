from abc import ABC, abstractmethod
from publisher import Publisher

class Product(ABC):

    product_id = 0  # Used for assigning incrementing IDs to ALL Product objects

    def __init__(self, title, price, publisher):

        # Type checking for all parameters
        if not isinstance(title, str):
            raise TypeError("Title parameter must be a string.")
        if not isinstance(price, (int, float)):
            raise TypeError("Price parameter is measured in dollars ($) and must be an integer or float number.")
        if not isinstance(publisher, Publisher):
            raise TypeError("Publisher parameter must be a Publisher object.")

        self.__title = title
        self.__price = price  # Measured in dollars ($)
        self.__publisher = publisher

        # Increments the product ID by 1 and assigns it to the private attribute "id"
        Product.product_id += 1
        self.__id = Product.product_id

    def get_title(self):
        return self.__title

    def get_price(self):
        return self.__price

    def get_publisher(self):
        return self.__publisher

    def get_id(self):
        return self.__id

    title = property(get_title)
    price = property(get_price)
    publisher = property(get_publisher)
    id = property(get_id)

    # This will be implemented by all concrete child classes, giving the details of the game/artwork/soundtrack/etc.
    @abstractmethod
    def get_details(self):
        pass