from undead import Undead

class CursedUndead(Undead):

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)

    def command(self):
        super().command()
        print(f"The {self.name} does cursed things...")