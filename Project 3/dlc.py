from abc import ABC
from product import Product
from game import Game

class DLC(Product, ABC):

    def __init__(self, title, price, publisher, base_game):
        super().__init__(title, price, publisher)

        # Type checking for all new parameters
        if not isinstance(base_game, Game):
            raise TypeError("Base game parameter must be a Game object.")

        self.__base_game = base_game

    def get_base_game(self):
        return self.__base_game

    base_game = property(get_base_game)
