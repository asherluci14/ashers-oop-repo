class Undead:
    """
        Intended as the base class for all undead minion types, holding shared stats and behaviours

        Attributes:
            MIN_HEALTH (int): Minimum base health (0)
            MAX_HEALTH (int): Maximum base health (100)
            MIN_POWER (int): Minimum base power (0)
            MAX_POWER (int): Maximum base power (100)
            MAX_LEVEL (int): Maximum level attainable (100)
            HEALTH_PER_LEVEL (int): Amount of health gained per level (2)
            POWER_PER_LEVEL (int): Amount of power gained per level (2)
            STARTING_LEVEL (int): Initial level of the creature (1)
            id (int): Unique identifier for the minion
            name (str): The name of the minion
            health (int): The current health value
            power (int): The current power value
            level (int): The current level

        Methods:
            level_up(): Increases the creature's level and boosts its health and power stats
            command(): Issues an order or action to the undead creature
    """

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
            # Prints custom messages based on which parameters are under/over
            # Uses if statements because all applicable issues should be addressed at once

            if health < self.MIN_HEALTH:
                print(f"Health for \"{name}\" must be at least {self.MIN_HEALTH}. You cannot set it to {health}.")

            if health > self.MAX_HEALTH:
                print(f"Health for \"{name}\" cannot exceed {self.MAX_HEALTH}. You cannot set it to {health}.")

            if power < self.MIN_POWER:
                print(f"Power for \"{name}\" must be at least {self.MIN_POWER}. You cannot set it to {power}.")

            if power > self.MAX_POWER:
                print(f"Power for \"{name}\" cannot exceed {self.MAX_POWER}. You cannot set it to {power}.")

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

    # Levels up the undead, if no argument is provided it levels it up by 1 level
    def level_up(self, new_levels=1):

        if not isinstance(new_levels, int):
            print(f"Level must be an integer. Level up for {self.name} was unsuccessful.")
            return False
        else:

            # For health and power, it adds (HEALTH/POWER)_PER_LEVEL) multiplied by how many levels to go up by
            new_level = self.level + new_levels
            new_health = self.health + (new_levels * self.HEALTH_PER_LEVEL)
            new_power = self.power + (new_levels * self.POWER_PER_LEVEL)

            # First checks if any conditions are true, and then prints ALL applicable conditions
            if (
                new_level > self.MAX_LEVEL
                or new_health > self.MAX_HEALTH
                or new_power > self.MAX_POWER
            ):
                print(f"\nYou cannot level up \"{self.name}\":\n")
                if new_level > self.MAX_LEVEL:
                    print(f"- New level ({new_level}) cannot exceed max level ({self.MAX_LEVEL}).")
                if new_health > self.MAX_HEALTH:
                    print(f"- New health ({new_health}) cannot exceed max health ({self.MAX_HEALTH}).")
                if new_power > self.MAX_POWER:
                    print(f"- New power ({new_power}) cannot exceed max power ({self.MAX_POWER}).")

                print("\nLevel up was unsuccessful. Please try different parameters.\n")

                return False

            else:
                self.__level = new_level
                self.__health = new_health
                self.__power = new_power

                print(f"\n\"{self.name}\" (id: {self.id}) was levelled up by {new_levels} level(s).\n")

                return True

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

    def command(self):
        print(f"The {self.name} does generic undead behaviour...")

    # Read-only properties
    id = property(get_id)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)