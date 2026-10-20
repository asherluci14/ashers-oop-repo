from abc import ABC, abstractmethod


class Exercise:

    def __init__(self, name, energy_cost):
        self.__name = name
        self.__energy_cost = energy_cost

    def get_name(self):
        return self.__name

    def get_energy_cost(self):
        return self.__energy_cost

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_energy_cost(self, energy_cost):
        if isinstance(energy_cost, (int, float)):
            self.__energy_cost = energy_cost

    name = property(get_name, set_name)
    energy_cost = property(get_energy_cost, set_energy_cost)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__name} costs {self.__energy_cost} energy."


class Member(ABC):

    def __init__(self, name, stamina):
        self.__name = name
        self.__stamina = stamina

    def get_name(self):
        return self.__name

    def get_stamina(self):
        return self.__stamina

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_stamina(self, stamina):
        if isinstance(stamina, (int, float)):
            self.__stamina = stamina

    name = property(get_name, set_name)
    stamina = property(get_stamina, set_stamina)

    @abstractmethod
    def perform_exercise(self, exercise):
        pass

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} has {self.stamina} stamina."


class StrengthMember(Member):

    def __init__(self, name, stamina, max_lift):
        super().__init__(name, stamina)
        self.__max_lift = max_lift

    def get_max_lift(self):
        return self.__max_lift

    def set_max_lift(self, max_lift):
        if isinstance(max_lift, (int, float)):
            self.__max_lift = max_lift

    max_lift = property(get_max_lift, set_max_lift)


class BeginnerLifter(StrengthMember):

    def __init__(self, name, stamina, max_lift):
        super().__init__(name, stamina, max_lift)

    def perform_exercise(self, exercise):
        if isinstance(exercise, Exercise):
            stamina_used = exercise.get_energy_cost()
            self.set_stamina(self.stamina - stamina_used)
            return (
                f"{self.name} completes {exercise.name} and loses "
                f"{stamina_used} stamina."
            )
        return "That is not a valid exercise."


class AdvancedLifter(StrengthMember):

    def __init__(self, name, stamina, max_lift):
        super().__init__(name, stamina, max_lift)

    def perform_exercise(self, exercise):
        if isinstance(exercise, Exercise):
            stamina_used = exercise.get_energy_cost() / 2
            self.set_stamina(self.stamina - stamina_used)
            return (
                f"{self.name} efficiently completes {exercise.name} and loses "
                f"{stamina_used} stamina."
            )
        return "That is not a valid exercise."


class WorkoutPlan:
    def __init__(self, title):
        self.__title = title
        self.__exercises = []

    def get_title(self):
        return self.__title

    def set_title(self, title):
        if isinstance(title, str):
            self.__title = title

    title = property(get_title, set_title)

    def create_exercise(self, name, energy_cost):
        exercise = Exercise(name, energy_cost)
        self.__exercises.append(exercise)
        return exercise

    def run_plan(self, member):

        if isinstance(member, Member):
            if len(self.__exercises) == 0:
                return f"{self.title} has no exercises."

            output = f"{member.name} starts the {self.title} plan.\n"

            for exercise in self.__exercises:
                output += member.perform_exercise(exercise) + "\n"

            return output.strip()
        else:
            return "not a valid member"

    def __str__(self):
        output = f"WorkoutPlan: {self.title}\n"

        if len(self.__exercises) == 0:
            output += "No exercises added."
        else:
            for exercise in self.__exercises:
                output += f"- {exercise}\n"

        return output.strip()


plan = WorkoutPlan("Full Body Blast")
beginner_lifter = BeginnerLifter("Sam", 105.9, 56)
advanced_lifter = AdvancedLifter("Jordan", 105.9, 129)
exercise_1 = plan.create_exercise("Deadlift", 10)
exercise_2 = plan.create_exercise("Bicep Curl", 38)