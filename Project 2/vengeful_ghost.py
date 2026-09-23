from cursed_undead import CursedUndead

class VengefulGhost(CursedUndead):
    """
        Intended to represent a spectral minion focusing heavily on cursed magical attacks

        Attributes:
            MIN_HEALTH (int): Minimum health (0)
            MAX_HEALTH (int): Maximum health (100)
            MIN_POWER (int): Minimum power (0)
            MAX_POWER (int): Maximum power (80)
            Inherits all other general attributes from CursedUndead

        Methods:
            Inherits all methods from the CursedUndead parent class
    """

    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 80

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)
