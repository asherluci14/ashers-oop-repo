from abc import ABC, abstractmethod

class UserGeneratedContent(ABC):

    def __init__(self, title, author, game):
        self.__title = title
        self.__author = author
        self.__game = game