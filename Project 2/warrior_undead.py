from undead import Undead

class WarriorUndead(Undead):

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)

    def command(self):
        super().command()
        print(f"The {self.name} does warrior-like things...")

    def combat_style(self):
        print(f"This undead specialises in direct martial combat.")
