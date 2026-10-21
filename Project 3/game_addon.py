from dlc import DLC

class GameAddon(DLC):

    def __init__(self, title, price, publisher, base_game, file_size):
        super().__init__(title, price, publisher, base_game)

        # Type checking for all new parameters
        if not isinstance(file_size, str):
            raise TypeError("File size parameter is measured in megabytes (MB) and must be an integer.")

        self.__file_size = file_size  # File size of the Game Addon, measured in MB

    def __str__(self):
        return (f"A Game Addon DLC titled \"{self.title}\" with ID {self.id}. Belongs to the game {self.base_game}. "
                f"Published by {self.publisher.name}. {self.file_size} MB. Listed at ${self.price}.")

    def get_file_size(self):
        return self.__file_size

    file_size = property(get_file_size)

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nProduct type: Game Addon (DLC)"
                         f"\nBase game: \"{self.base_game}\""
                         f"\nPrice: ${self.price}"
                         f"\nPublisher: {self.publisher.name}"
                         f"\nFile size: {self.file_size} MB")

        return return_string
