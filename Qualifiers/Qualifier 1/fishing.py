# A fishing rod is used to catch fish and can have an attached lure

import random

class Lure:

    def __init__(self, type, description):
        self.__type = type
        self.__description = description

    def __str__(self):
        return f"A {self.__type} type lure. {self.__description}"

    def get_description(self):
        return self.__description

    def get_type(self):
        return self.__type


class FishingRod:

    def __init__(self, type, durability=100, lure=None):
        self.__type = type
        self.set_durability(durability)

        self.lure = lure

    def get_durability(self):
        return self.__durability

    def set_durability(self, new_value):
        if new_value < 0:
            self.__durability = 0
        elif new_value > 100:
            self.__durability = 100
        else:
            self.__durability = new_value

    def cast(self):
        durability = self.get_durability()

        if durability <= 0:
            print("The rod is already broken.")
            return False
        else:
            damage = random.randint(0, 10)
            new_durability = self.get_durability() - damage
            self.set_durability(new_durability)

            if self.lure is None:
                print("no lure")
                return False
            else:
                print("line was thrown")
                return True

    def check_requires_repair(self):
        if self.get_durability() <= 0:
            print("broken")
            return True
        else:
            return False

    def repair_rod(self):
        self.set_durability(100)

    def check_durability(self):
        durability = self.get_durability()

        if durability <= 25:
            return "is damaged"
        elif durability <= 50:
            return "is in okay condition"
        elif durability <= 75:
            return "is in great condition"
        else:
            return "is in excellent condition"

    def attach_lure(self, lure):
        if isinstance(lure, Lure):
            self.lure = lure
        else:
            print("Attached lure must be of the type \"Lure\".")

    def __str__(self):
        lure_text = "has" if (self.lure is not None) else "doesn't have"
        main_info = f"A {self.__type} rod which {self.check_durability()}.\nIt {lure_text} a lure attached."
        lure_description = ""

        if self.lure is not None:
            lure_description = f" It uses a {self.lure.get_type()} lure. {self.lure.get_description()}."

        return main_info + lure_description


lure_1 = Lure("Sparkly", "It spins to attract fish")  # Used with fishing rod 1
fishing_rod_1 = FishingRod("Telescopic")

lure_2 = Lure("Spinner", "It flashes light to attract fish")  # Used with fishing rod 2
fishing_rod_2 = FishingRod("Wooden", 0, None)

fishing_rod_1.cast()
fishing_rod_1.attach_lure(lure_1)
fishing_rod_1.cast()
update_1 = str(fishing_rod_1)

update_2 = str(fishing_rod_2)

fishing_rod_2.attach_lure(lure_2)
update_3 = str(fishing_rod_2)

fishing_rod_2.repair_rod()
fishing_rod_2.cast()