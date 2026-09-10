from warrior_undead import WarriorUndead

class SkeletonWarrior(WarriorUndead):

    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 100

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)

