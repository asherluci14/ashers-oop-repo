from game_addon import GameAddon

class WorkshopMod(GameAddon):

    def __init__(self, title, price, publisher, base_game, file_size, version):
        super().__init__(title, price, publisher, base_game, file_size)

        # TODO: Import UGC once it's created

        # Type checking for all new parameters
        if not isinstance(version, str):
            raise TypeError("Version parameter must be a string (e.g. \"1.8.9\").")

        self.__version = version  # Version of the workshop mod
        self.__subscribers = set()  # An empty set where subscribers will be added

    def __str__(self):
        return (f"A Workshop Mod titled \"{self.title}\", version {self.version} with ID {self.id}. "
                f"Belongs to the game {self.base_game}. "
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
