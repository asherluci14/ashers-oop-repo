# Implement your code here
class Layer:

    def __init__(self, size: int, flavour: str):
        self.size = size
        self.__flavour = flavour
        self.is_baked = False  # Should always be False upon construction

    def __str__(self):
        return f"{str(self.size)}\" {self.get_flavour()} tier."

    def get_flavour(self):
        return self.__flavour

    def set_flavour(self, new_flavour):
        if self.is_baked:
            print("This layer is already baked, you cannot change the flavour.")
        else:
            if isinstance(new_flavour, str):
                self.__flavour = new_flavour

    def bake(self):
        if not self.is_baked:
            self.is_baked = True
            print(f"3, 2, 1... *Ding* The {self.get_flavour()} tier is ready.")
        else:
            print("This layer is already baked!")


class Cake:

    def __init__(self):
        self.__tiers = []  # Start with an empty list of tiers

    def __str__(self):
        tier_count = str(len(self.__tiers))
        head = f"A {tier_count} tier celebration cake made of:"

        layer_list = ""

        for layer in self.__tiers:
            layer_list += f"\n- {str(layer)}"

        return head + layer_list

    def add_tier(self, new_layer):
        if isinstance(new_layer, Layer):
            if new_layer in self.__tiers:
                print("This layer is already in the cake!")
            else:
                if new_layer.is_baked:
                    self.__tiers.append(new_layer)
                else:
                    print("I should bake this first.")


layer_1 = Layer(11, 'Chocolate')
layer_2 = Layer(10, 'Red Velvet')
layer_3 = Layer(7, 'Red Velvet')
cake = Cake()

print(layer_1)
print(layer_2)
print(layer_3)

cake.add_tier(layer_1)

layer_1.bake()
layer_2.bake()
layer_3.bake()

cake.add_tier(layer_1)
cake.add_tier(layer_2)
cake.add_tier(layer_3)

print(cake)