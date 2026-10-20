from abc import ABC, abstractmethod


class Event:
    def __init__(self, name, dress_code):
        self.__name = "unnamed event"
        self.__dress_code = "unknown"
        self.set_name(name)
        self.set_dress_code(dress_code)

    def get_name(self):
        return self.__name

    def get_dress_code(self):
        return self.__dress_code

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def set_dress_code(self, dress_code):
        if isinstance(dress_code, str):
            self.__dress_code = dress_code

    name = property(get_name, set_name)
    dress_code = property(get_dress_code, set_dress_code)

    def __str__(self):
        return f"{self.__class__.__name__}: {self.__name} ({self.__dress_code})"


# --------------------------------------------------
# Clothing classes
# --------------------------------------------------

class Clothing(ABC):

    def __init__(self, colour, material):
        self.__colour = "unknown"
        self.__material = "unknown"
        self.set_colour(colour)
        self.set_material(material)

    def get_colour(self):
        return self.__colour

    def get_material(self):
        return self.__material

    def set_colour(self, colour):
        if isinstance(colour, str):
            self.__colour = colour

    def set_material(self, material):
        if isinstance(material, str):
            self.__material = material

    colour = property(get_colour, set_colour)
    material = property(get_material, set_material)

    @abstractmethod
    def style_for(self, event):
        pass


class Top(Clothing):

    def __init__(self, colour, material, sleeve):
        super().__init__(colour, material)
        self.__sleeve = "unknown"
        self.set_sleeve(sleeve)

    def get_sleeve(self):
        return self.__sleeve

    def set_sleeve(self, sleeve):
        if isinstance(sleeve, str):
            self.__sleeve = sleeve

    sleeve = property(get_sleeve, set_sleeve)


class Shirt(Top):

    def __init__(self, colour, material, sleeve):
        super().__init__(colour, material, sleeve)

    def style_for(self, event):
        if isinstance(event, Event):
            if event.get_dress_code().lower() == "formal":
                return (
                    f"The {self.__class__.__name__} can be tucked in with tailored trousers "
                    f"for {event.get_name()}."
                )
            return (
                f"The {self.__class__.__name__} works well with relaxed styling for "
                f"{event.get_name()}."
            )
        else:
            return "Invalid event"

    def __str__(self):
        return f"Shirt: {self.colour}, {self.material}, {self.sleeve} sleeves"


class Hoodie(Top):

    def __init__(self, colour, material, sleeve):
        super().__init__(colour, material, sleeve)

    def style_for(self, event):
        if isinstance(event, Event):
            if event.get_dress_code().lower() == "formal":
                return (
                    f"The {self.__class__.__name__} is generally too casual for "
                    f"{event.get_name()}."
                )
            return (
                f"The {self.__class__.__name__} pairs well with casual outfits for "
                f"{event.get_name()}."
            )
        else:
            return "Invalid event"

    def __str__(self):
        return f"Hoodie: {self.colour}, {self.material}, {self.sleeve} sleeves"


class Outfit:
    def __init__(self, name):
        self.__name = "unnamed"
        self.__clothes = []
        self.set_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    name = property(get_name, set_name)

    def create_clothing(self, clothing_type, colour, material, sleeve):

        if clothing_type.lower().strip() == "shirt":
            shirt = Shirt(colour, material, sleeve)
            self.__clothes.append(shirt)
            return shirt
        elif clothing_type.lower().strip() == "hoodie":
            hoodie = Hoodie(colour, material, sleeve)
            self.__clothes.append(hoodie)
            return hoodie
        else:
            return None

    def style_for_event(self, event):

        if isinstance(event, Event):
            if len(self.__clothes) == 0:
                return f"{self.__name} has no clothing."

            description = f"{self.__name} styled for {event.get_name()}:\n"

            for clothing in self.__clothes:
                description += f"- {clothing.style_for(event)}\n"

            return description.strip()
        else:
            return "Invalid event"

    def __str__(self):
        if len(self.__clothes) == 0:
            return f"{self.__name} has no clothing."

        description = f"Outfit: {self.__name}\n"
        for clothing in self.__clothes:
            description += f"- {clothing}\n"

        return description.strip()


# --------------------------------------------------
# Example usage
# --------------------------------------------------

event = Event("Casual Dinner", "Casual")
outfit = Outfit("Smart Outfit")
shirt = outfit.create_clothing("Shirt", "Black", "Cotton", "Sleeveless")
hoodie = outfit.create_clothing("Hoodie", "Grey", "Denim", "Short")