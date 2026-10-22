class Store:
    instance = None  # Class-level variable to hold the single instance

    def __new__(cls, name="Steam"):

        # Create the instance ONLY if it doesn't already exist
        if cls.instance is None:
            # Put very simply, this allocates the memory for the instance
            cls.instance = super(Store, cls).__new__(cls)

            # This is here because the store gets renamed every time Store() is instantiated if it's in the __init__()
            cls.instance.__name = name
            cls.instance.__catalogue = []
            cls.instance.__delisted_products = []

        # If it's the first time initialising Store() it creates, saves, and returns it
        # If Store() has already been initialised once, it just skips creation and return the original Store object
        return cls.instance

    # Initialises the store. Only one store can exist in this system.
    def __init__(self, name="Steam"):
        # __new__() handles everything, the __init__() does not need any new code
        pass

    def __str__(self):
        pass
        # TODO: i'll do this later

    def get_name(self):
        return self.__name

    def get_catalogue(self):
        return self.__catalogue

    def get_delisted_products(self):
        return self.__delisted_products

    name = property(get_name)
    catalogue = property(get_catalogue)
    delisted_products = property(get_delisted_products)

    def add_product(self, product):
        """Adds a new Product into the store catalogue."""

        # Deferred import to avoid circular import errors
        from product import Product

        # Type checking before a product is added to the store's catalogue (where users browse from)
        if not isinstance(product, Product):
            raise TypeError("Catalogue can only contain valid Product objects.")

        # Ensures duplicate objects aren't added
        if product not in self.__catalogue and product not in self.__delisted_products:
            self.__catalogue.append(product)

    def delist_product(self, product):
        """Removes a Product from the public catalogue, preventing it from being purchased."""

        # Type checking isn't needed because the catalogue can only have Product items inside

        # Removes product from the catalogue
        if product in self.__catalogue:
            self.__catalogue.remove(product)

            # Adds product to the delisted list
            if product not in self.__delisted_products:
                self.__delisted_products.append(product)

    def relist_product(self, product):
        """Re-adds a previously delisted Product back into the store catalogue."""

        # If it was delisted, it's removed from the delisted list
        if product in self.__delisted_products:
            self.__delisted_products.remove(product)

        # Re-adds to the public catalogue
        # add_product() already handles both the type checking and the duplicate check
        self.add_product(product)

    # Private helper method -- shouldn't be used outside of this class
    def __display_products(self, product_list):
        """Private helper method to avoid repeating display logic."""

        if len(product_list) == 0:
            print("No products found.")

        else:

            # Can apply to Store.catalogue or Store.delisted_products
            for product in product_list:
                print(product.get_details())
                print("-" * 40)  # Visual separator between products

    def display(self):
        """Displays all active products currently for sale in the store."""

        print(f"=== {self.name} Store Catalogue ===")
        self.__display_products(self.__catalogue)

    def display_delisted(self):
        """Displays all delisted products."""

        print(f"=== {self.name} Delisted Archive ===")
        self.__display_products(self.__delisted_products)

    def search_catalogue(self, keyword: str):
        """Searches the public catalogue for products containing the keyword in any attribute."""

        if not isinstance(keyword, str):
            raise TypeError("Search keyword must be a string.")

        keyword = keyword.lower().strip()
        matching_products = []

        # Uses the concrete classes' implementation of get_details() to search for the keyword
        for product in self.__catalogue:

            details = product.get_details().lower().strip()

            if keyword in details:
                matching_products.append(product)

        self.__display_products(matching_products)

        return matching_products

    def search_title(self, keyword: str):
        """Searches the public catalogue for products containing the keyword in the title."""

        if not isinstance(keyword, str):
            raise TypeError("Search keyword must be a string.")

        keyword = keyword.lower().strip()
        matching_products = []

        # Uses the Products' title attribute to search their titles for the keyword
        for product in self.__catalogue:

            if keyword in product.title.lower().strip():
                matching_products.append(product)

        self.__display_products(matching_products)

        return matching_products