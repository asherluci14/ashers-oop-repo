from resource_manager import ResourceManager
from undead import Undead
from skeleton_warrior import SkeletonWarrior
from phantom_guardian import PhantomGuardian
from vengeful_ghost import VengefulGhost
from putrid_zombie import PutridZombie
from death_knight import DeathKnight

class SummoningRitual:
    """
        Intended to define the costs and logic for performing a ritual to create a specific undead creature

        Attributes:
            existing_rituals (list): The current ectoplasm costs for each ritual so far
            name (str): The name of the ritual
            undead_name (str): The "species" name of the undead that will be summoned
            starting_health (int): The initial health assigned to the summoned creature
            starting_power (int): The initial power assigned to the summoned creature
            necrotic_cost (int): The number of necrotic runes required
            spirit_cost (int): The number of spirit runes required
            bone_cost (int): The number of bone runes required
            flesh_cost (int): The number of flesh runes required
            ectoplasm_cost (int): The amount of ectoplasm required

        Methods:
            can_perform(): Checks if the ritual conditions and resource costs are met
            perform(): Executes the ritual process
            create_undead(): Creates and returns a new Undead instance
    """

    existing_rituals = []

    def __init__(self, name, undead_name, starting_health, starting_power, necrotic_cost, spirit_cost,
                 bone_cost, flesh_cost, ectoplasm_cost):

        ritual_costs = [necrotic_cost, spirit_cost, bone_cost, flesh_cost, ectoplasm_cost]

        all_integers = True

        if ectoplasm_cost <= 0:  # Ensures every ritual requires ectoplasm
            print(f"Ectoplasm cost for {undead_name} must be at least 1.")
        elif ritual_costs in self.existing_rituals:  # Ensures two rituals don't have the same costs
            print("There is already a ritual with these resource costs.")
        else:

            for item in ritual_costs:
                if not isinstance(item, int):
                    all_integers = False

            if not isinstance(starting_health, int) or not isinstance(starting_power, int):
                all_integers = False

            if not all_integers:
                print("All provided health/power/resources values must be integers.")
                print(f"Summoning ritual \"{name}\" could not be instantiated.")
            else:
                self.__name = name
                self.__undead_name = undead_name
                self.__starting_health = starting_health
                self.__starting_power = starting_power

                self.__necrotic_cost = necrotic_cost
                self.__spirit_cost = spirit_cost
                self.__bone_cost = bone_cost
                self.__flesh_cost = flesh_cost
                self.__ectoplasm_cost = ectoplasm_cost

                # Adds ritual costs to existing rituals
                self.existing_rituals.append(ritual_costs)

    def get_name(self):
        return self.__name

    def get_undead_name(self):
        return self.__undead_name

    def get_starting_health(self):
        return self.__starting_health

    def get_starting_power(self):
        return self.__starting_power

    def get_necrotic_cost(self):
        return self.__necrotic_cost

    def get_spirit_cost(self):
        return self.__spirit_cost

    def get_bone_cost(self):
        return self.__bone_cost

    def get_flesh_cost(self):
        return self.__flesh_cost

    def get_ectoplasm_cost(self):
        return self.__ectoplasm_cost

    # This checks if the provided resource manager has enough resources to complete the smell
    def can_perform(self, resource_object):

        if isinstance(resource_object, ResourceManager):
            if resource_object.has_resources(
                self.__necrotic_cost,
                self.__spirit_cost,
                self.__bone_cost,
                self.__flesh_cost,
                self.__ectoplasm_cost
            ):
                return True
            else:
                return False
        else:
            print("Provided argument must be a ResourceManager object.")
            return False

    def perform(self, resource_object):

        if isinstance(resource_object, ResourceManager):
            resource_object.spend_resources(
                self.__necrotic_cost,
                self.__spirit_cost,
                self.__bone_cost,
                self.__flesh_cost,
                self.__ectoplasm_cost
            )

            return True
        else:
            print("Provided argument must be a ResourceManager object.")
            return False

    def create_undead(self, id):
        if self.undead_name == "Skeleton Warrior":
            return SkeletonWarrior(id, self.__undead_name, self.__starting_health, self.__starting_power)
        elif self.undead_name == "Phantom Guardian":
            return PhantomGuardian(id, self.__undead_name, self.__starting_health, self.__starting_power)
        elif self.undead_name == "Vengeful Ghost":
            return VengefulGhost(id, self.__undead_name, self.__starting_health, self.__starting_power)
        elif self.undead_name == "Putrid Zombie":
            return PutridZombie(id, self.__undead_name, self.__starting_health, self.__starting_power)
        elif self.undead_name == "Death Knight":
            return DeathKnight(id, self.__undead_name, self.__starting_health, self.__starting_power)
        else:
            return Undead(id, self.__undead_name, self.__starting_health, self.__starting_power)

    # Read-only properties
    name = property(get_name)
    undead_name = property(get_undead_name)
    starting_health = property(get_starting_health)
    starting_power = property(get_starting_power)

    necrotic_cost = property(get_necrotic_cost)
    spirit_cost = property(get_spirit_cost)
    bone_cost = property(get_bone_cost)
    flesh_cost = property(get_flesh_cost)
    ectoplasm_cost = property(get_ectoplasm_cost)