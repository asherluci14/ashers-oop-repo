from product import Product

class Game(Product):

    def __init__(self, title, price, publisher, version, file_size):
        super().__init__(title, price, publisher)

        # Type checking for all new parameters
        if not isinstance(version, str):
            raise TypeError("Version parameter must be a string.")
        if not isinstance(file_size, int):
            raise TypeError("File size parameter is measured in MB and must be an integer.")

        self.__version = version
        self.__file_size = file_size  # The file size is measured in megabytes (MB)
        self.__dlc_list = []  # A list where DLCs can be added for the game

    def __str__(self):
        return (f"A game titled \"{self.title}\", version {self.version} with ID {self.id}. "
                f"Published by {self.publisher.name}. {self.file_size} MB. Listed at ${self.price}.")

    def get_version(self):
        return self.__version

    def get_file_size(self):
        return self.__file_size

    def get_dlc_list(self):
        return self.__dlc_list

    version = property(get_version)
    file_size = property(get_file_size)
    dlc_list = property(get_dlc_list)

    def get_details(self) -> str:
        return_string = (f"\"{self.title}\""
                         f"\nProduct type: Game"
                         f"\nPrice: ${self.price}"
                         f"\nPublisher: {self.publisher.name}"
                         f"\nVersion: {self.version}"
                         f"\nFile size: {self.file_size} MB"
                         f"\nDLCs available: {len(self.dlc_list)}")

        return return_string

    # Adds a DLC to the DLC list
    def add_dlc(self, dlc) -> bool:

        # Deferred import to avoid circular import errors
        from dlc import DLC

        # First checks if the passed parameter is a DLC object
        if not isinstance(dlc, DLC):

            # Sends a warning message instead of raising a TypeError so the user can try again instead of crashing
            print("The DLC parameter must be a DLC object. Please try again.")
            return False

        # Appends the DLC to the DLC list
        self.__dlc_list.append(dlc)
        return True

    def list_dlcs(self) -> str:

        dlc_count = len(self.__dlc_list)

        if dlc_count == 0:
            # Returns a unique string if no DLCs have been added to the game
            return f"The game {self.title} has no DLCs."

        else:
            return_string = f"The game {self.title} has {dlc_count} listed DLCs:"

            for dlc in self.__dlc_list:

                dlc_type = "DLC"

                # Identifies the type of DLC by looking at that subclass's attributes (each has unique attributes)
                if hasattr(dlc, "version"):
                    dlc_type = "Workshop Mod"
                elif hasattr(dlc, "file_size"):
                    dlc_type = "Game Addon"
                elif hasattr(dlc, "resolution"):
                    dlc_type = "Artwork"
                elif hasattr(dlc, "tracks"):
                    dlc_type = "Soundtrack"

                return_string += f"\n - {dlc.title} ({dlc_type}) -- ${dlc.price}"

            return return_string
