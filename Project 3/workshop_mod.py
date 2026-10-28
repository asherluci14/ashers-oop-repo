from game_addon import GameAddon
from user_generated_content import UserGeneratedContent
from user import User

class WorkshopMod(GameAddon, UserGeneratedContent):

    def __init__(self, title, price, publisher, base_game, file_size, version, author):

        # Explicitly calling parent initialisers because multiple inheritance is used
        GameAddon.__init__(self, title=title, price=price, publisher=publisher,
                           base_game=base_game, file_size=file_size)
        UserGeneratedContent.__init__(self, title=title, author=author, game=base_game)

        # Type checking for all new parameters
        if not isinstance(version, str):
            raise TypeError("Version parameter must be a string (e.g. \"1.8.9\").")

        self.__version = version  # Version of the workshop mod
        self.__subscribers = set()  # An empty set where subscribers will be added

    def __str__(self):
        return (f"A Workshop Mod titled \"{self.title}\", version {self.version} with ID {self.id}. "
                f"Belongs to the game {self.base_game}. Created by user {self.author.username}. "
                f"Published by {self.publisher.name}. {self.file_size} MB. Listed at ${self.price}.")

    def get_version(self):
        return self.__version

    def get_subscribers(self):
        return self.__subscribers

    version = property(get_version)
    subscribers = property(get_subscribers)

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nProduct type: Workshop Mod (DLC/UGC)"
                         f"\nBase game: \"{self.base_game.title}\""
                         f"\nPrice: ${self.price}"
                         f"\nPublisher: {self.publisher.name}"
                         f"\nVersion: {self.version}"
                         f"\nFile size: {self.file_size} MB"
                         f"\nSubscribers: {len(self.subscribers)}")

        return return_string

    def add_subscriber(self, user):
        """Adds a subscriber to the workshop mod's current set of subscribers."""

        # Type checking
        if not isinstance(user, User):
            raise TypeError("Added subscriber must be a User object.")

        # Adds the user to the private set of subscribers
        self.__subscribers.add(user)

    def remove_subscriber(self, user):
        """Removes a subscriber from the workshop mod's current set of subscribers."""

        # Removes the user from the subscriber set if they're already in it
        if user in self.__subscribers:
            self.__subscribers.discard(user)  # .discard() is used to a KeyError isn't thrown (for edge cases)

    def list_subscribers(self) -> str:

        # Returns specific string if there are no subscribers
        if len(self.__subscribers) == 0:
            return f"Workshop mod \"{self.title}\" has no subscribers yet."

        else:
            # Sorts the set alphabetically (and turns it into a list as a result)
            # Lambda function is used to specify to sort by the username of the User objects
            alphabetical = sorted(self.__subscribers, key=lambda u: u.username)

            return_string = f"All subscribers for workshop mod \"{self.title}\":"

            for user in alphabetical:
                return_string += f"\n - {user.username}"

            return return_string
