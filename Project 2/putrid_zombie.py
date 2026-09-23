from undead import Undead

class PutridZombie(Undead):
    """
        Intended to represent a basic zombie minion with lower power and modest health limits

        Attributes:
            MIN_HEALTH (int): Minimum health (0)
            MAX_HEALTH (int): Maximum health (80)
            MIN_POWER (int): Minimum power (0)
            MAX_POWER (int): Maximum power (20)
            Inherits all other general attributes from Undead

        Methods:
            Inherits all methods from the Undead parent class
    """

    MIN_HEALTH = 0
    MAX_HEALTH = 80
    MIN_POWER = 0
    MAX_POWER = 20

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)
