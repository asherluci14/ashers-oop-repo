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

    def get_necrotic_runes(self):
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

    necrotic_runes = property(get_necrotic_runes)
    spirit_runes = property(get_spirit_runes)
    bone_runes = property(get_bone_runes)
    flesh_runes = property(get_flesh_runes)
    ectoplasm = property(get_ectoplasm)


class Undead:

    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER =0

    def __init__(self, id, name, health, power, level):
        pass















thing = ResourceManager(-5,1,2,34,2)
print(repr(thing))

print(thing.flesh_runes)
print(thing)