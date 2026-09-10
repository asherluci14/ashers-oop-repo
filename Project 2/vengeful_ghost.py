from cursed_undead import CursedUndead

class VengefulGhost(CursedUndead):

    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 80

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)
