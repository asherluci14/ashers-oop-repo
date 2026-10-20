class CommunityHub:
    instance = None  # Class-level variable to hold the single instance

    def __new__(cls):

        # Create the instance ONLY if it doesn't already exist
        if cls.instance is None:
            cls.instance = super(CommunityHub, cls).__new__(cls)  # Basically this allocates the memory for the instance

        # If it's the first time initialising CommunityHub() it creates, saves, and returns it
        # If it's already been initialised once, it just skips creation and return the original object
        return cls.instance

    # Initialises the community hub. Only one community hub can exist in this system.
    def __init__(self):

        # Prevent re-initialising attributes if the singleton already exists
        if not hasattr(self, 'initialized'):
            self.__all_ugc = []
            self.initialized = True  # It doesn't really matter what you set this to; __init__ checks for existence

    def add_content(self, content):
        # TODO: Add type checking
        self.__all_ugc.append(content)

    def remove_content(self, content):
        if content in self.__all_ugc:
            self.__all_ugc.remove(content)