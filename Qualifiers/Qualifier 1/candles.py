# Candles have wax and a wick
# Burn time depends on both wax type and wick length

import math

class Wax:

    def __init__(self, type):
        self.__type = type
        self.__burn_time = self.calculate_burn_time(type)

    def __str__(self):
        return f"{self.__type} wax, with burn factor {self.get_burn_time()}."

    def calculate_burn_time(self, type):
        if type == "Bee":
            return 1.1
        elif type == "Paraffin":
            return 1.2
        elif type == "Soy":
            return 1.4
        else:
            return 1.7

    def get_burn_time(self):
        return self.__burn_time


class Wick:

    def __init__(self, length):
        self.__length = length  # In centimeters
        self.__burn_time = self.calculate_burn_time(length)

    def __str__(self):
        return f"A {self.__length} wick, with burn factor {self.get_burn_time()}."

    def calculate_burn_time(self, length):
        burn_time = round((length * math.pi), 2)
        return burn_time

    def get_burn_time(self):
        return self.__burn_time


class Candle:

    def __init__(self, size, wax, wick, is_lit=False):
        self.__size = size
        self.__wax = wax
        self.__wick = wick
        self.is_lit = is_lit

        self.__burn_time = self.calculate_burn_time()

    def __str__(self):
        return f"A {self.__size} candle, with burn factor {self.get_burn_time()}."

    def calculate_burn_time(self):
        wax_time = self.__wax.get_burn_time()
        wick_time = self.__wick.get_burn_time()
        burn_time = round((wax_time * wick_time), 2)
        return burn_time

    def light(self):
        self.is_lit = True

    def extinguish(self):
        self.is_lit = False

    def get_size(self):
        return self.__size

    def set_size(self, new_size):
        if self.is_lit:
            print("A lit candle can't be safely reshaped.")
        else:
            self.__size = new_size

    def get_burn_time(self):
        return self.__burn_time


wax_1 = Wax("Paraffin")
wax_2 = Wax("Bee")
wax_3 = Wax("Soy")

wick_1 = Wick(6.0)
wick_2 = Wick(7.0)
wick_3 = Wick(2.0)

candle_1 = Candle("large", wax_1, wick_1)
candle_2 = Candle("medium", wax_2, wick_2)
candle_3 = Candle("small", wax_3, wick_3)

print(wax_1)
print(wick_1)
print(candle_1)