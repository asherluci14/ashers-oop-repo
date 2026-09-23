from undead import Undead

class WarriorUndead(Undead):
    """
        Intended as an undead subclass specialised in physical and martial combat styles

        Attributes:
            Inherits all attributes from the Undead parent class

        Methods:
            command(): Issues an order tailored to martial undead creatures
            combat_style(): Executes or returns the physical combat style of the minion
    """

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)

    def command(self):
        super().command()
        print(f"The {self.name} does warrior-like things...")

    def combat_style(self):
        print(f"This undead specialises in direct martial combat.")
