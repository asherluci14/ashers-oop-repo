from resource_manager import ResourceManager
from summoning_ritual import SummoningRitual
from undead import Undead

class Necromancer:
    """
        Intended to represent a necromancer entity who can manage resources and summon undead minions

        Attributes:
            MAX_UNDEAD (int): The maximum number of undead creatures allowed (20)
            name (str): The name of the necromancer
            level (int): The current level of the necromancer
            resources (list): The resource manager or collection of resources owned by the necromancer
            undead (list): The list holding all current summoned undead creatures
            summon_id (int): Number for keeping track of IDs of summoned undead

        Methods:
            summon(): Summons a new undead creature into the necromancer's service
            dismiss(): Dismisses an existing undead creature from the necromancer's collection
            level_undead(): Levels up an undead along with their health and power
            find_undead(): Returns the Undead object with the matching ID
    """

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

        # Checks if necromancer already has maximum undead capacity and prevents exceeding it
        if len(self.undead) >= self.MAX_UNDEAD:
            print(f"Necromancer \"{self.name}\" already has the maximum amount of undead ({self.MAX_UNDEAD})!")
            print("Try dismissing existing undead then try again.")
            return False
        else:

            if isinstance(ritual, SummoningRitual):

                if ritual.can_perform(self.__resources):

                    # create_undead() may fail. This does error checking so that it is appended to the
                    # Necromancer's list ONLY IF it is a valid object

                    new_undead = ritual.create_undead(self.__summon_id + 1)

                    # This ensures the instantiation worked before any major changes are made
                    if new_undead is not None and hasattr(new_undead, 'id'):
                        ritual.perform(self.__resources)  # This spends the resources but doesn't create the undead
                        self.__summon_id += 1  # ID is incremented by 1 across the whole class

                        # A new undead is created and appended to the necromancer's list
                        self.__undead.append(new_undead)

                        return True

                    else:
                        print("Summoning ritual failed to create a valid undead.")
                        return False

                else:
                    print("You do not have enough resources to cast this ritual.")
                    return False

            else:
                print("The passed argument must be a SummoningRitual object.")
                return False

    # Dismisses an undead based on its ID
    def dismiss(self, searched_id):
        undead = self.find_undead(searched_id)

        if isinstance(undead, Undead):
            self.__undead.remove(undead)  # Removes the first (and only) undead with the matching ID from the list
            print(f"Undead {searched_id} was dismissed.")
            return True
        else:
            print(f"The dismissal of undead with ID {searched_id} was unsuccessful.")
            return False

    # Levels up an undead based on its ID
    def level_undead(self, searched_id, new_levels):

        # Finds the specific undead object based on its ID
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

    # Returns the Undead object with the matching ID
    def find_undead(self, searched_id):
        if isinstance(searched_id, int):

            if len(self.__undead) > 0:
                for undead in self.__undead:
                    if undead.id == searched_id:
                        return undead

                print(f"An undead with the ID {searched_id} could not be found.")
                return None
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
