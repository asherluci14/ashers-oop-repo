from dlc import DLC

class Soundtrack(DLC):

    def __init__(self, title, price, publisher, base_game, tracks, length):
        super().__init__(title, price, publisher, base_game)

        # Type checking for all new parameters
        if not isinstance(tracks, int) or isinstance(tracks, bool):
            raise TypeError("Tracks parameter must be an integer.")
        if not isinstance(length, (int, float)) or isinstance(length, bool):
            raise TypeError("Length parameter is measured in minutes and must be an integer or a float.")

        self.__tracks = tracks  # Number of tracks in the soundtrack
        self.__length = length  # Total length of the soundtrack, measured in minutes

    def __str__(self):
        return (f"A Soundtrack DLC titled \"{self.title}\" with ID {self.id}. Belongs to the game {self.base_game}. "
                f"Has {self.tracks} tracks in total. {self.length} minutes long. "
                f"Published by {self.publisher.name}. Listed at ${self.price}.")

    def get_tracks(self):
        return self.__tracks

    def get_length(self):
        return self.__length

    tracks = property(get_tracks)
    length = property(get_length)

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nProduct type: Soundtrack (DLC)"
                         f"\nBase game: \"{self.base_game.title}\""
                         f"\nPrice: ${self.price}"
                         f"\nPublisher: {self.publisher.name}"
                         f"\nTracks: {self.tracks}"
                         f"\nLength: {self.length} minutes")

        return return_string
