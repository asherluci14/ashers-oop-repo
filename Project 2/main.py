class ResourceManager:

    MIN_RESOURCES = 0

    def __init__(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):

        # Must be INTEGER and quantities should not begin below 0
        # TODO: Not allowed to raise errors yet -- fix later

        resources = [
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm
        ]

        # Goes through the list of inputted resources, and if it's less than 0 it just sets it to 0
        for i in range(len(resources)):
            if not isinstance(resources[i], int) or resources[i] < self.MIN_RESOURCES:
                print(f"Resource quantity must be an integer greater than or equal to {self.MIN_RESOURCES}.")
                resources[i] = self.MIN_RESOURCES

        # The entered and edited values are set as instance variables
        self.__necrotic_runes = resources[0]
        self.__spirit_runes = resources[1]
        self.__bone_runes = resources[2]
        self.__flesh_runes = resources[3]
        self.__ectoplasm = resources[4]

    # TODO: Enter real data
    def __str__(self):

        return_text = f"The following resources are available:"
        return_text += f"\n - {self.__necrotic_runes} necrotic runes"
        return_text += f"\n - {self.__spirit_runes} spirit runes"
        return_text += f"\n - {self.__bone_runes} bone runes"
        return_text += f"\n - {self.__flesh_runes} flesh runes"
        return_text += f"\n - {self.__ectoplasm} ectoplasm"

        return return_text

    def __repr__(self):
        return (f"ResourceManager({self.__necrotic_runes}, {self.__spirit_runes}, {self.__bone_runes}, "
                f"{self.__flesh_runes}, {self.__ectoplasm})")

    def get_necrotic_runes(self) -> int:
        return self.__necrotic_runes

    def get_spirit_runes(self):
        return self.__spirit_runes

    def get_bone_runes(self):
        return self.__bone_runes

    def get_flesh_runes(self):
        return self.__flesh_runes

    def get_ectoplasm(self):
        return self.__ectoplasm

    def collect(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):

        # Must be INTEGER and quantities should not begin below 0
        # TODO: Not allowed to raise errors yet -- fix later

        insufficient_resources = False

        resources = [
            necrotic_runes,
            spirit_runes,
            bone_runes,
            flesh_runes,
            ectoplasm
        ]

        # Goes through the list of inputted resources, and if it's less than 0 it just sets it to 0
        for i in range(len(resources)):
            if not isinstance(resources[i], int) or resources[i] < 0:
                print("Resource quantity must be an integer greater than or equal to 0.")
                resources[i] = 0
                insufficient_resources = True

        # The entered and edited values are added to the current resource pool
        self.__necrotic_runes += resources[0]
        self.__spirit_runes += resources[1]
        self.__bone_runes += resources[2]
        self.__flesh_runes += resources[3]
        self.__ectoplasm += resources[4]

        # Prints a notification message if any values were not updated
        if insufficient_resources:
            print("Any values that were provided that were under 0 were not updated.")

    def has_resources(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):

        # Returns True if all values are available, returns False if any are unavailable
        if (self.__necrotic_runes >= necrotic_runes
            and self.__spirit_runes >= spirit_runes
            and self.__bone_runes >= bone_runes
            and self.__flesh_runes >= flesh_runes
            and self.__ectoplasm >= ectoplasm
        ):
            return True
        else:
            return False

    def spend_resources(self, necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):

        # Validates that that many resources exist to begin with, then decreases them from the instance variable
        if self.has_resources(necrotic_runes, spirit_runes, bone_runes, flesh_runes, ectoplasm):
            self.__necrotic_runes -= necrotic_runes
            self.__spirit_runes -= spirit_runes
            self.__bone_runes -= bone_runes
            self.__flesh_runes -= flesh_runes
            self.__ectoplasm -= ectoplasm
        else:
            print("You do not have enough resources.")

    # Read-only properties
    necrotic_runes = property(get_necrotic_runes)
    spirit_runes = property(get_spirit_runes)
    bone_runes = property(get_bone_runes)
    flesh_runes = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)


class Undead:

    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 100
    MAX_LEVEL = 100
    HEALTH_PER_LEVEL = 2
    POWER_PER_LEVEL = 2
    STARTING_LEVEL = 1

    def __init__(self, id, name, health, power):

        if not isinstance(health, int):
            print("Health must be an integer.")
        elif not isinstance(power, int):
            print("Power must be an integer.")
        elif not isinstance(name, str):
            print("Name must be a string.")
        elif (
            health < self.MIN_HEALTH
            or health > self.MAX_HEALTH
            or power < self.MIN_POWER
            or power > self.MAX_POWER
        ):
            print("Health and power must be within boundary limits.")
        else:
            self.__id = id
            self.__name = name
            self.__health = health
            self.__power = power
            self.__level = self.STARTING_LEVEL  # Level should always start at 1

            print(f"{name} created successfully.")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def get_power(self):
        return self.__power

    def get_level(self):
        return self.__level

    def level_up(self, level, health, power):

        # Checks that the new values will not exceed the maximum allowed values
        if (self.__level + level) > self.MAX_LEVEL:
            print(f"Level cannot exceed {self.MAX_LEVEL}.")
        elif (self.__health + health) > self.MAX_HEALTH:
            print(f"Health level cannot exceed {self.MAX_HEALTH}.")
        elif (self.__power + power) > self.MAX_POWER:
            print(f"Power level cannot exceed {self.MAX_POWER}.")
        else:
            # Data type is validated before making any changes
            if (
                isinstance(level, int)
                and isinstance(health, int)
                and isinstance(power, int)
            ):
                self.__level += level
                self.__health += health
                self.__power += power
            else:
                print("Please provide appropriate data types for each argument (all must be integers).")

    def __str__(self):
        return_text = f"An undead entity with the following properties:"
        return_text += f"\n - id: {self.__id}"
        return_text += f"\n - name: {self.__name}"
        return_text += f"\n - level: {self.__level}"
        return_text += f"\n - health: {self.__health} / {self.MAX_HEALTH}"
        return_text += f"\n - power: {self.__power} / {self.MAX_POWER}"
        return return_text

    def __repr__(self):
        return (f"Undead(id={self.__id}, name='{self.__name}', health={self.__health}, "
                f"power={self.__power}, level={self.__level})")

    # Read-only properties
    id = property(get_id)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)


class SummoningRitual:

    existing_rituals = []

    def __init__(self, name, undead_name, starting_health, starting_power, necrotic_cost, spirit_cost,
                 bone_cost, flesh_cost, ectoplasm_cost):

        ritual_costs = [necrotic_cost, spirit_cost, bone_cost, flesh_cost, ectoplasm_cost]

        if ectoplasm_cost <= 0:  # Ensures every ritual requires ectoplasm
            print(f"Ectoplasm cost for {undead_name} must be at least 1.")
        elif ritual_costs in self.existing_rituals:  # Ensures two rituals don't have the same costs
            print("There is already a ritual with these resource costs.")
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
    def level_undead(self, searched_id, level, health, power):

        undead = self.find_undead(searched_id)

        if isinstance(undead, Undead):
            undead.level_up(level, health, power)
            print(f"Undead {searched_id} was levelled up.")
            return True
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
                return False  # Not sure whether to return False or None
            else:
                print("There are currently no undead being controlled by this necromancer.")
                return False

        else:
            print("ID provided must be an integer.")
            return False

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



# --------------------------------------------------------------------

# 1. Undead Skeleton Warrior (Low-cost physical unit)
skeleton_warrior = SummoningRitual(
    name="Skeleton Warrior",
    undead_name="Skeleton Warrior",
    starting_health=100,
    starting_power=15,
    necrotic_cost=10,
    spirit_cost=0,
    bone_cost=50,
    flesh_cost=0,
    ectoplasm_cost=10
)

# 2. Vengeful Ghost (High-spirit/ectoplasm magic unit)
vengeful_ghost = SummoningRitual(
    name="Vengeful Ghost",
    undead_name="Vengeful Ghost",
    starting_health=60,
    starting_power=30,
    necrotic_cost=15,
    spirit_cost=40,
    bone_cost=0,
    flesh_cost=0,
    ectoplasm_cost=40
)

# 3. Putrid Zombie (High-health tank unit)
putrid_zombie = SummoningRitual(
    name="Putrid Zombie",
    undead_name="Putrid Zombie",
    starting_health=90,
    starting_power=10,
    necrotic_cost=20,
    spirit_cost=0,
    bone_cost=10,
    flesh_cost=60,
    ectoplasm_cost=30
)

# 4. Phantom Guardian (Elite hybrid unit)
phantom_guardian = SummoningRitual(
    name="Phantom Guardian",
    undead_name="Phantom Guardian",
    starting_health=100,
    starting_power=60,
    necrotic_cost=30,
    spirit_cost=30,
    bone_cost=25,
    flesh_cost=0,
    ectoplasm_cost=100
)


necro = Necromancer("Asher")
necro.resources.collect(10000,10000,10000,0,10000)

print(necro.resources)
necro.summon(phantom_guardian)
print(necro.resources)
necro.summon(vengeful_ghost)
print(necro.resources)

necro.summon(putrid_zombie)
print(necro.resources)

necro.resources.collect(0,0,0,10000,0)
necro.summon(putrid_zombie)
print(necro.resources)

print(necro.find_undead(1))
necro.level_undead(1, 29, 0, 20)
print(necro.find_undead(1))

print(necro.find_undead(2))
necro.dismiss(2)
print(necro.find_undead(2))

print(necro)
