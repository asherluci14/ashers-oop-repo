from warrior_undead import WarriorUndead

class SkeletonWarrior(WarriorUndead):
    """
        Intended to represent a basic physical warrior minion built on skeletal remains

        Attributes:
            MIN_HEALTH (int): Minimum health (0)
            MAX_HEALTH (int): Maximum health (100)
            MIN_POWER (int): Minimum power (0)
            MAX_POWER (int): Maximum power (100)
            Inherits all other general attributes from WarriorUndead

        Methods:
            Inherits all methods from the WarriorUndead parent class
    """

    # These are actually the same as the default, but can be customised
    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 100

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)
