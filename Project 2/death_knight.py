from warrior_undead import WarriorUndead
from cursed_undead import CursedUndead

class DeathKnight(WarriorUndead, CursedUndead):
    """
        Intended to represent a powerful hybrid elite unit combining both martial combat and cursed abilities

        Attributes:
            MIN_HEALTH (int): Minimum health (100)
            MAX_HEALTH (int): Maximum health (400)
            MIN_POWER (int): Minimum power (100)
            MAX_POWER (int): Maximum power (400)
            HEALTH_PER_LEVEL (int): Health gained per level (5)
            POWER_PER_LEVEL (int): Power gained per level (5)
            STARTING_LEVEL (int): Initial starting level (5)

        Methods:
            combat_style(): Executes or returns the hybrid knight combat style
            compare_combat_styles(): Compares this minion's combat style with another unit's style
            command(): Issues a high-level command to the Death Knight
    """

    MIN_HEALTH = 100
    MAX_HEALTH = 400
    MIN_POWER = 100
    MAX_POWER = 400
    STARTING_LEVEL = 5
    HEALTH_PER_LEVEL = 5
    POWER_PER_LEVEL = 5

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)

    def combat_style(self):
        super().combat_style()

    def compare_combat_styles(self):
        WarriorUndead.combat_style(self)
        CursedUndead.combat_style(self)

    # Added in the Code Review, not part of the specifications itself
    def command(self):
        super().command()
