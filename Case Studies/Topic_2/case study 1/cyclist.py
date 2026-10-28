class Cyclist:

    valid_turns = ['right', 'left']

    def __init__(self, name, age, weight, proficiency, protective_gear=False):
        self.name = name
        self.age = age
        self.weight = weight
        self.proficiency = proficiency
        self.protective_gear = protective_gear

    def __str__(self):
        text = 'with' if self.protective_gear else 'without'
        return f"A {self.age}y/o {self.weight}kg {self.proficiency} cyclist named {self.name}, {text} protection gear."

    def __repr__(self):
        return f"Cyclist({self.name}, {self.age}, {self.weight}, {self.proficiency}, {self.protective_gear})"

    def accelerate(self):
        print(f"{self.name} is going forward!")

    def brake(self):
        print(f"{self.name} is stopping!")

    def turn(self, direction):
        if isinstance(direction, str) and direction.lower().strip() in Cyclist.valid_turns:
            print(f"{self.name} is turning {direction}.")

    def toggle_protection(self):
        self.protective_gear = not self.protective_gear  # Simple toggle
        text = 'is now' if self.protective_gear else 'is now not'
        print(f"{self.name} {text} wearing protective gear.")

