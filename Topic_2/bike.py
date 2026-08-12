class Bike:
    def __init__(self, bike_type, maximum_gears):
        self.bike_type = bike_type
        self.maximum_gears = maximum_gears
        self.current_gear = 1

    def __str__(self):
        return f"A {self.bike_type} bike, set on gear {self.current_gear} out of {self.maximum_gears} maximum gears."

    def __repr__(self):
        return f"Bike({self.bike_type}, {self.maximum_gears}, current_gear = {self.current_gear})"

    def change_gear(self, increase: bool):
        if increase:
            if self.current_gear == self.maximum_gears:
                print(f"You have reached the maximum gear for this bike ({self.maximum_gears}).")
            else:
                self.current_gear += 1
                print(f"The new gear is: {self.current_gear}.")
        elif not increase:
            if self.current_gear == 1:
                print("You cannot lower the gear any further.")
            else:
                self.current_gear -= 1
                print(f"The new gear is: {self.current_gear}.")

