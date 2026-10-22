from user_generated_content import UserGeneratedContent
from store import Store

class CommunityHub:
    instance = None  # Class-level variable to hold the single instance

    def __new__(cls):

        # Create the instance ONLY if it doesn't already exist
        if cls.instance is None:
            cls.instance = super(CommunityHub, cls).__new__(cls)  # Basically this allocates the memory for the instance

            cls.instance.__feed = []

        # If it's the first time initialising CommunityHub() it creates, saves, and returns it
        # If it's already been initialised once, it just skips creation and return the original object
        return cls.instance

    # Initialises the community hub. Only one community hub can exist in this system.
    def __init__(self):
        # __new__() handles everything, the __init__() does not need any new code
        pass

    def get_feed(self):
        return self.__feed

    feed = property(get_feed)

    def add_content(self, content):
        """"Adds a UserGeneratedContent item to the global community feed."""

        # Type checking
        if not isinstance(content, UserGeneratedContent):
            raise TypeError("Content parameter must be a UserGeneratedContent object.")

        # Ensures duplicate objects aren't added
        if content not in self.__feed:
            self.__feed.append(content)

    def remove_content(self, content):
        """Removes a UserGeneratedContent item from the global feed."""

        if content in self.__feed:
            self.__feed.remove(content)

    def display_feed(self):
        """Displays all global community content in a timeline format."""

        store = Store()

        print(f"=== {store.name} Community Feed ===")

        if len(self.__feed) == 0:
            print("No community posts found.")
        else:

            for content in self.__feed:
                print(content.get_details())
                print("-" * 40)  # Visual separator