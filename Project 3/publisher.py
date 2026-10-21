class Publisher:

    publisher_id = 0  # Used for assigning incrementing IDs to all Publisher objects

    def __init__(self, name):

        if not isinstance(name, str):
            raise TypeError("Name must be a string.")

        self.__name = name

        # Increments the publisher ID by 1 and assigns it to the private attribute "id"
        Publisher.publisher_id += 1
        self.__id = Publisher.publisher_id

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__id

    name = property(get_name)
    id = property(get_id)