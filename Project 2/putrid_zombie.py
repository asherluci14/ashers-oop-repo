from undead import Undead

class PutridZombie(Undead):

    MIN_HEALTH = 0
    MAX_HEALTH = 80
    MIN_POWER = 0
    MAX_POWER = 20

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)
