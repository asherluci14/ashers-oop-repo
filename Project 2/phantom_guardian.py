from warrior_undead import WarriorUndead

class PhantomGuardian(WarriorUndead):
    """
        Intended to represent a highly defensive physical warrior minion with higher health and power caps

        Attributes:
            MIN_HEALTH (int): Minimum health (0)
            MAX_HEALTH (int): Maximum health (200)
            MIN_POWER (int): Minimum power (0)
            MAX_POWER (int): Maximum power (200)
            Inherits all other general attributes from WarriorUndead

        Methods:
            Inherits all methods from the WarriorUndead parent class
    """

    MIN_HEALTH = 0
    MAX_HEALTH = 200
    MIN_POWER = 0
    MAX_POWER = 200

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)
