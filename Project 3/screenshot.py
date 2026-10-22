from user_generated_content import UserGeneratedContent

class Screenshot(UserGeneratedContent):

    def __init__(self, title, author, game, resolution):
        super().__init__(title, author, game)

        # Type checking for all new parameters
        if not isinstance(resolution, str):
            raise TypeError("Resolution parameter must be a string (e.g. 1920x1080).")

        self.__resolution = resolution  # Resolution of the screenshot (e.g. 3840x2160)

    def get_resolution(self):
        return self.__resolution

    resolution = property(get_resolution)

    def __str__(self):
        return (f"A Screenshot titled \"{self.title}\" with ID {self.id} for the game \"{self.game.title}\". "
                f"Captured by {self.author.username} at {self.resolution} resolution.")

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nContent type: Screenshot"
                         f"\nGame: \"{self.game.title}\""
                         f"\nAuthor: {self.author.username}"
                         f"\nResolution: {self.resolution}")

        return return_string