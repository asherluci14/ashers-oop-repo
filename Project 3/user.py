from library import Library
from store import Store
from dlc import DLC
from product import Product
from community_hub import CommunityHub

class User:

    user_id = 0  # Used for assigning incrementing IDs to all User objects

    def __init__(self, username: str, wallet: int | float):

        # Type checking for all parameters
        if not isinstance(username, str):
            raise TypeError("Username parameter must be a string.")
        if not isinstance(wallet, (int, float)) or isinstance(wallet, bool):
            raise TypeError("Wallet parameter is measured in dollars ($) and must be an integer or float number.")

        self.__username = username
        self.__wallet = wallet  # Measured in dollars ($), can be a float or integer
        self.__library = Library()  # The library is created by the user (composition)
        self.__subscribed_mods = set()  # Empty set where the user's subscribed mods will go

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

    def get_subscribed_mods(self):
        return self.__subscribed_mods

    username = property(get_username)
    wallet = property(get_wallet)
    library = property(get_library)
    subscribed_mods = property(get_subscribed_mods)

    def add_funds(self, amount: int | float):
        """Allows the user to add funds (in dollars ($) at a time) to their personal wallet."""

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            raise TypeError(f"Amount parameter is measured in dollars ($) and must be an integer or float number.")

        self.__wallet += amount

    def purchase_product(self, product) -> bool:
        """Allows the user to purchase a product from the store catalogue."""

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

    # This is a private method because it should not be used by any external classes
    def __post_ugc(self, content):
        """Private method used to help post user generated content to the community hub."""

        # Deferred import to avoid circular import errors
        from user_generated_content import UserGeneratedContent

        # Strictly speaking this is not necessary because it will only ever be used in the post_* methods where
        # there's type checking at object __init__(), but theoretically you could pass a non-product object in
        if not isinstance(content, UserGeneratedContent):
            raise TypeError("Object must be a valid UserGeneratedContent instance.")

        # User does not store this content internally

        # The store class is a singleton so when we instantiate it, it creates/gives the first reference
        CommunityHub().add_content(content)

        return content

    def post_discussion(self, title, text, game):
        """Allows the user to create and publish a discussion."""

        # Deferred import to avoid circular import errors (just in case)
        from discussion import Discussion

        # No need for more type checking because it's already done inside the __init__() method
        discussion = Discussion(title=title, text=text, game=game, author=self)

        # Passes it to the private helper to register it in the CommunityHub
        return self.__post_ugc(discussion)

    def post_review(self, title, text, rating, recommend, game):
        """Allows the user to create and publish a review."""

        # Deferred import to avoid circular import errors (just in case)
        from review import Review

        # No need for more type checking because it's already done inside the __init__() method
        review = Review(title=title, text=text, rating=rating, recommend=recommend, game=game, author=self)

        # Passes it to the private helper to register it in the CommunityHub
        return self.__post_ugc(review)

    def post_video(self, title, length, resolution, game):
        """Allows the user to create and publish a video."""

        # Deferred import to avoid circular import errors (just in case)
        from video import Video

        # No need for more type checking because it's already done inside the __init__() method
        video = Video(title=title, length=length, resolution=resolution, game=game, author=self)

        # Passes it to the private helper to register it in the CommunityHub
        return self.__post_ugc(video)

    def post_screenshot(self, title, resolution, game):
        """Allows the user to create and publish a screenshot."""

        # Deferred import to avoid circular import errors (just in case)
        from screenshot import Screenshot

        # No need for more type checking because it's already done inside the __init__() method
        screenshot = Screenshot(title=title, resolution=resolution, game=game, author=self)

        # Passes it to the private helper to register it in the CommunityHub
        return self.__post_ugc(screenshot)

    def post_workshop_mod(self, title, price, game, file_size, publisher, version):
        """Allows the user to create and publish a workshop mod."""

        # Deferred import to avoid circular import errors (just in case)
        from workshop_mod import WorkshopMod

        # No need for more type checking because it's already done inside the __init__() method
        mod = WorkshopMod(title=title, price=price, publisher=publisher, base_game=game, file_size=file_size,
                          version=version, author=self)

        # Passes it to the private helper to register it in the CommunityHub
        return self.__post_ugc(mod)

    def subscribe_to_mod(self, mod) -> bool:
        """Allows the user to subscribe to a workshop mod."""

        # Deferred import to avoid circular import errors (just in case)
        from workshop_mod import WorkshopMod

        # Type checking
        if not isinstance(mod, WorkshopMod):
            raise TypeError("Mod parameter must be a WorkshopMod object.")

        # Checks that the user owns the required base game
        if not self.__library.has_product(mod.base_game):
            print(f"Cannot subscribe to '{mod.title}': You must own the base game '{mod.base_game.title}' first!")
            return False

        # Add to the user's personal subscribed mods set
        self.__subscribed_mods.add(mod)

        # Register the user as a subscriber on the mod side as well
        mod.add_subscriber(self)

        # Prints a success message
        print(f"{self.username} successfully subscribed to workshop mod \"{mod.title}\"!")
        return True

    def unsubscribe_from_mod(self, mod) -> bool:
        """Allows the user to unsubscribe from a workshop mod."""

        # Deferred import to avoid circular import errors (just in case)
        from workshop_mod import WorkshopMod

        # Type checking
        if not isinstance(mod, WorkshopMod):
            raise TypeError("Mod parameter must be a WorkshopMod object.")

        # Checks that the user is already subscribed to the mod
        if not mod in self.__subscribed_mods:
            print(f"Cannot unsubscribe from '{mod.title}': You are not subscribed to begin with!")
            return False

        # Discard from the user's subscribed mods set (safe against KeyError)
        self.__subscribed_mods.discard(mod)

        # Remove the user from the mod's subscriber set
        mod.remove_subscriber(self)

        print(f"{self.username} unsubscribed from workshop mod \"{mod.title}\".")
        return True
