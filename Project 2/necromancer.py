from resource_manager import ResourceManager
from summoning_ritual import SummoningRitual
from undead import Undead

class Necromancer:

    MAX_UNDEAD = 20  # The max number of undead that can be controlled by one necromancer

    def __init__(self, name):

        if not isinstance(name, str):
            print("The name must be a string.")
        else:
            self.__name = name
            self.__resources = ResourceManager(0,0,0,0,0)
            self.__undead = []
            self.__summon_id = 0  # Should increment by 1 for each new summon created

    def get_name(self):
        return self.__name

    def get_resources(self):
        return self.__resources

    def get_undead(self):
        return self.__undead

    def summon(self, ritual):
        if isinstance(ritual, SummoningRitual):

            if ritual.can_perform(self.__resources):
                ritual.perform(self.__resources)  # All this does is spend the resources but doesn't create the undead

                self.__summon_id += 1  # ID is incremented by 1

                # A new undead is created and appended to the necromancer's list
                self.__undead.append(ritual.create_undead(self.__summon_id))

            else:
                print("You do not have enough resources to cast this ritual.")

        else:
            print("The passed argument must be a SummoningRitual object.")

    # Dismisses an undead based on its id
    def dismiss(self, searched_id):
        undead = self.find_undead(searched_id)

        if isinstance(undead, Undead):
            self.__undead.remove(undead)  # Removes the first (and only) undead with the matching ID from the list
            print(f"Undead {searched_id} was dismissed.")
            return True
        else:
            print(f"The dismissal of undead with ID {searched_id} was unsuccessful.")
            return False

    # Levels up an undead based on its id
    def level_undead(self, searched_id, new_levels):

        undead = self.find_undead(searched_id)

        if isinstance(undead, Undead):
            result = undead.level_up(new_levels)

            # Errors can occur inside undead.level_up(new_levels), so it will only return True if it was successful
            if result:
                return True
            else:
                return False

        else:
            print(f"The levelling up of undead with ID {searched_id} was unsuccessful.")
            return False

    def find_undead(self, searched_id):
        if isinstance(searched_id, int):

            if len(self.__undead) > 0:
                for undead in self.__undead:
                    if undead.id == searched_id:
                        return undead

                print(f"An undead with the ID {searched_id} could not be found.")
                return None  # Not sure whether to return False or None
            else:
                print("There are currently no undead being controlled by this necromancer.")
                return None

        else:
            print("ID provided must be an integer.")
            return None

    def __str__(self):
        return_string = f"For the necromancer {self.__name}:\n"
        return_string += str(self.__resources)
        return_string += f"\n\nThey also own the following undead:\n"
        return_string += str(self.__undead)
        return return_string

    # Read-only properties
    name = property(get_name)
    resources = property(get_resources)
    undead = property(get_undead)