from store import Store

class Publisher:

    publisher_id = 0  # Used for assigning incrementing IDs to all Publisher objects

    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        self.__name = name

        # Increments the publisher ID by 1 and assigns it to the private attribute "id"
        Publisher.publisher_id += 1
        self.__id = Publisher.publisher_id

        self.__products = []  # Tracks the products published by this publisher

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    def get_products(self):
        return self.__products

    name = property(get_name)
    id = property(get_id)
    products = property(get_products)

    # This is a private method because it should not be used by any external classes
    def __push_publication(self, product):

        # Deferred import to avoid circular import errors
        from product import Product

        # Strictly speaking this is not necessary because it will only ever be used in the publish_* methods where
        # there's type checking at object __init__(), but theoretically you could pass a non-product object in
        if not isinstance(product, Product):
            raise TypeError("Object must be a valid Product instance.")

        # Adds the product to the Publisher.__products list
        self.__products.append(product)

        # The store class is a singleton so when we instantiate it, it creates/gives the first reference
        Store().add_product(product)

        return product


    # The following methods publish Products by 1) adding them to self.__products and 2) listing them in the Store
    # This is done by instantiating the specified object, then putting it through __push_publication().

    def publish_game(self, title, price, version, file_size):

        # Deferred import to avoid circular import errors
        from game import Game

        # No need for more type checking because it's already done inside the __init__() method
        game = Game(title=title, price=price, publisher=self, version=version, file_size=file_size)

        # Passes it to the private helper to register it in the local list and in the Store
        return self.__push_publication(game)

    def publish_addon(self, title, price, base_game, file_size):

        # Deferred import to avoid circular import errors
        from game_addon import GameAddon

        # No need for more type checking because it's already done inside the __init__() method
        addon = GameAddon(title=title, price=price, publisher=self, base_game=base_game, file_size=file_size)

        # Passes it to the private helper to register it in the local list and in the Store
        return self.__push_publication(addon)

    def publish_artwork(self, title, price, base_game, resolution):

        # Deferred import to avoid circular import errors
        from artwork import Artwork

        # No need for more type checking because it's already done inside the __init__() method
        artwork = Artwork(title=title, price=price, publisher=self, base_game=base_game, resolution=resolution)

        # Passes it to the private helper to register it in the local list and in the Store
        return self.__push_publication(artwork)

    def publish_soundtrack(self, title, price, base_game, tracks, length):

        # Deferred import to avoid circular import errors
        from soundtrack import Soundtrack

        # No need for more type checking because it's already done inside the __init__() method
        soundtrack = Soundtrack(title=title, price=price, publisher=self, base_game=base_game, tracks=tracks,
                                length=length)

        # Passes it to the private helper to register it in the local list and in the Store
        return self.__push_publication(soundtrack)
