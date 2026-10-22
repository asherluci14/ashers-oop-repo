from user_generated_content import UserGeneratedContent

class Discussion(UserGeneratedContent):

    def __init__(self, title, author, game, text):
        super().__init__(title, author, game)

        # Type checking for all new parameters
        if not isinstance(text, str):
            raise TypeError("Text parameter must be a string.")

        self.__text = text  # The main body text of the discussion post

    def get_text(self):
        return self.__text

    text = property(get_text)

    def __str__(self):
        return (f"A Discussion thread titled \"{self.title}\" with ID {self.id} for the game \"{self.game.title}\". "
                f"Started by {self.author.username}.")

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nContent type: Discussion"
                         f"\nGame: \"{self.game.title}\""
                         f"\nAuthor: {self.author.username}"
                         f"\nPost Text: \"{self.text}\"")

        return return_string