class Store:
    instance = None  # Class-level variable to hold the single instance

    def __new__(cls, name):

        # Create the instance ONLY if it doesn't already exist
        if cls.instance is None:
            cls.instance = super(Store, cls).__new__(cls)  # Put very simply, this allocates the memory for the instance

        # If it's the first time initialising Store() it creates, saves, and returns it
        # If Store() has already been initialised once, it just skips creation and return the original Store object
        return cls.instance

    # Initialises the store. Only one store can exist in this system.
    def __init__(self, name="Steam"):

        # Prevent re-initialising attributes if the singleton already exists
        if not hasattr(self, 'initialized'):
            self.name = name
            self.catalogue = []
            self.initialized = True  # It doesn't really matter what you set this to; __init__ checks for existence

    def add_product(self, product):
        # TODO: Add type checking
        self.catalogue.append(product)

    def remove_product(self, product):
        if product in self.catalogue:
            self.catalogue.remove(product)