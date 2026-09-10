class Undead:

    MIN_HEALTH = 0
    MAX_HEALTH = 100
    MIN_POWER = 0
    MAX_POWER = 100
    MAX_LEVEL = 100
    HEALTH_PER_LEVEL = 2  # What does this even do? It was not clear in the specifications and is unused currently
    POWER_PER_LEVEL = 2  # What does this even do? It was not clear in the specifications and is unused currently
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

    def command(self):
        print(f"The {self.name} does generic undead behaviour...")

    # Read-only properties
    id = property(get_id)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)