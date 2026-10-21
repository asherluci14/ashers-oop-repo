from publisher import Publisher
from game import Game
from dlc import DLC


p = Publisher("Team Cherry")
g = Game("Hollow Knight", 20, p, "1.0", 2000)
d = DLC("Hidden Dreams", 0, p, g)

print(g.list_dlcs())
g.add_dlc(d)
print(g.list_dlcs())
