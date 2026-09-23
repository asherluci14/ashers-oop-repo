from undead import Undead

class CursedUndead(Undead):
    """
        Intended as an undead subclass specialised in magic afflictions and cursed combat styles

        Attributes:
            Inherits all attributes from the Undead parent class

        Methods:
            command(): Issues an order tailored to cursed undead creatures
            combat_style(): Executes or returns the cursed combat style of the minion
    """

    def __init__(self, id, name, health, power):
        super().__init__(id, name, health, power)

    def command(self):
        super().command()
        print(f"The {self.name} does cursed things...")

    def combat_style(self):
        print(f"This undead specialises in cursed/supernatural combat.")
