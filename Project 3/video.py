from user_generated_content import UserGeneratedContent

class Video(UserGeneratedContent):

    def __init__(self, title, author, game, length, resolution):
        super().__init__(title, author, game)

        # Type checking for all new parameters
        if not isinstance(length, (int, float)):
            raise TypeError("Length parameter must be an integer or float number.")
        if not isinstance(resolution, str):
            raise TypeError("Resolution parameter must be a string (e.g. 1920x1080).")

        if length <= 0:
            raise ValueError("Video length must be greater than zero.")

        self.__length = length  # Duration of the video in seconds
        self.__resolution = resolution  # Resolution of the video (e.g. 1920x1080)

    def get_length(self):
        return self.__length

    def get_resolution(self):
        return self.__resolution

    length = property(get_length)
    resolution = property(get_resolution)

    def __str__(self):
        return (f"A Video titled \"{self.title}\" with ID {self.id} for the game \"{self.game.title}\". "
                f"Created by {self.author.username} with a length of {self.length}s and resolution {self.resolution}.")

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nContent type: Video"
                         f"\nGame: \"{self.game.title}\""
                         f"\nAuthor: {self.author.username}"
                         f"\nLength: {self.length} seconds"
                         f"\nResolution: {self.resolution}")

        return return_string