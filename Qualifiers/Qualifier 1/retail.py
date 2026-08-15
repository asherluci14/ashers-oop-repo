class Product:

    def __init__(self, id, rank, name=None):
        self.ID = id
        self.set_rank(rank)
        self.name = name

    def get_rank(self):
        return self.__rank

    def set_rank(self, new_rank):
        if 1 <= new_rank <= 10:
            self.__rank = new_rank
        else:
            self.__rank = 0

    def __str__(self):
        name = f"({self.name})" if self.name is not None else ""
        return f"Product {self.ID} {name}. Is ranked #{self.get_rank()}."


class Order:

    def __init__(self):
        self.__items = []

    def add_product(self, new_product):
        if isinstance(new_product, Product):
            self.__items.append(new_product)
        """
        else:
            print("New product must be of the type \"Product\".")
        """

    def top_10_product_count(self):  # Counts how many of the items in the order are in the top 10 rank
        count = 0
        for product in self.__items:
            if 1 <= product.get_rank() <= 10:
                count += 1

        return count

    def get_list_length(self):
        return len(self.__items)

    def __str__(self):
        return f"This order has {self.get_list_length()} items and has {self.top_10_product_count()} top 10 products."


product1 = Product("P277", 7)
product2 = Product("P469", 0, "Notebook")
my_order = Order()

my_order.add_product(product1)
my_order.add_product(product2)

print(my_order)