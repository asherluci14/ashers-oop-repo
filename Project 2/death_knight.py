from warrior_undead import WarriorUndead
from cursed_undead import CursedUndead

class DeathKnight(WarriorUndead, CursedUndead):

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
