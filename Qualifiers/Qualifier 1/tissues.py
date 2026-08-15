class Tissue:

    def __init__(self, ply, scent, is_hypoallergenic):
        self.__ply = ply
        self.__scent = scent
        self.__is_hypoallergenic = is_hypoallergenic

    def get_ply(self):
        return self.__ply

    def set_ply(self, new_ply):
        if isinstance(new_ply, int) and new_ply >= 1:
            self.__ply = new_ply

    def __str__(self):
        text = " hypoallergenic" if self.__is_hypoallergenic else ""
        return f"{self.__ply} ply{text} {self.__scent}-scented tissue"


class TissueBox:
    def __init__(self, maximum_tissue_count=10):
        self.maximum_tissue_count = maximum_tissue_count
        self.__tissues = []

    def count_tissues(self):
        return len(self.__tissues)

    def refill_maximum_tissues(self, tissue):
        if isinstance(tissue, Tissue):
            remaining_tissues = self.maximum_tissue_count - self.count_tissues()
            for i in range(remaining_tissues):
                self.__tissues.append(tissue)

    def refill_some_tissues(self, amount, tissue):
        if isinstance(tissue, Tissue):
            for i in range(amount):
                if self.count_tissues() == self.maximum_tissue_count:
                    break
                else:
                    self.__tissues.append(tissue)

    def take_single_tissue(self):
        if self.count_tissues() == 0:
            print("The box is empty.")
            return False
        else:
            print("You take a tissue.")
            self.__tissues.pop(-1)
            return True

    def take_multiple_tissues(self, amount):
        if self.count_tissues() == 0:
            print("The box is empty.")
            return False
        else:
            print(f"You take {amount} tissues.")
            for i in range(amount):
                self.__tissues.pop(-1)
            return True

    def __str__(self):
        if self.count_tissues() == 0:
            return f"The box is empty and does not contain tissues."
        else:
            return_text = ""
            for tissue in self.__tissues:
                return_text += str(tissue) + "\n"

            return return_text


tissue_1 = Tissue(6, "Citrus", True)
tissue_2 = Tissue(2, "Rose", True)
tissue_3 = Tissue(5, "Lavender", False)
tissue_box = TissueBox()

print(tissue_1)
print(tissue_2)
print(tissue_3)
print(tissue_box)

update_1 = str(tissue_box)

tissue_box.refill_some_tissues(4, tissue_1)
tissue_box.refill_some_tissues(3, tissue_2)
tissue_box.refill_maximum_tissues(tissue_3)
print(tissue_box)

update_2 = str(tissue_box)

tissue_box.take_single_tissue()
tissue_box.take_multiple_tissues(2)
print(tissue_box)

update_3 = str(tissue_box)

