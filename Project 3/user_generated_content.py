from abc import ABC, abstractmethod
from game import Game
from user import User

class UserGeneratedContent(ABC):

    ugc_id = 0  # Used for assigning incrementing IDs to all UGC objects

    def __init__(self, title, author, game):

        # Type checking for all parameters
        if not isinstance(title, str):
            raise TypeError("Title parameter must be a string.")
        if not isinstance(author, User):
            raise TypeError("Author parameter must be a User object.")
        if not isinstance(game, Game):
            raise TypeError("Game parameter must be a Game object.")

        self.__title = title
        self.__author = author
        self.__game = game

        # Increments the UGC ID by 1 and assigns it to the private attribute "id"
        UserGeneratedContent.ugc_id += 1
        self.__id = UserGeneratedContent.ugc_id

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_game(self):
        return self.__game

    def get_id(self):
        return self.__id

    title = property(get_title)
    author = property(get_author)
    game = property(get_game)
    id = property(get_id)

    # This will be implemented by all concrete child classes, giving the details of the video/screenshot/review/etc.
    @abstractmethod
    def get_details(self):
        pass
