from dlc import DLC

class Artwork(DLC):

    def __init__(self, title, price, publisher, base_game, resolution):
        super().__init__(title, price, publisher, base_game)

        # Type checking for all new parameters
        if not isinstance(resolution, str):
            raise TypeError("Resolution parameter is measured in pixels and must be a string (e.g. 1920x1080).")

        self.__resolution = resolution  # Resolution of the artwork, measured in pixels (e.g. 1920x1080)

    def __str__(self):
        return (f"An Artwork DLC titled \"{self.title}\" with ID {self.id}. Belongs to the game {self.base_game}. "
                f"Image resolution is {self.resolution} pixels. "
                f"Published by {self.publisher.name}. Listed at ${self.price}.")

    def get_resolution(self):
        return self.__resolution

    resolution = property(get_resolution)

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nProduct type: Artwork (DLC)"
                         f"\nBase game: \"{self.base_game.title}\""
                         f"\nPrice: ${self.price}"
                         f"\nPublisher: {self.publisher.name}"
                         f"\nResolution: {self.resolution} pixels")

        return return_string
