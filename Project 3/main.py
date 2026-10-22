from publisher import Publisher
from game import Game
from dlc import DLC
from store import Store  # Assuming your Store class is saved in store.py

# --- Existing DLC Testing ---
p = Publisher("Team Cherry")
g = Game("Hollow Knight", 20, p, "1.0", 2000)
d = DLC("Hidden Dreams", 0, p, g)

print("--- DLC Relationship Test ---")
print("Initial DLCs:", g.list_dlcs())
g.add_dlc(d)
print("After adding DLC:", g.list_dlcs())

print("\n" + "="*50 + "\n")

# --- Store Singleton & E-Commerce Testing ---
print("--- Store Singleton Test ---")
store1 = Store("Steam")
store2 = Store()  # Should point to the exact same instance!
print(f"Are store1 and store2 the exact same instance? {store1 is store2}")
print(f"Store Name: {store1.name}")

print("\n--- Adding Products to Store ---")
store1.add_product(g)
store1.add_product(d)

# Try adding a duplicate product (should be ignored safely)
store1.add_product(g)

# Display active store catalogue
store1.display()

print("\n" + "="*50 + "\n")

print("--- Delisting Test ---")
print("Delisting 'Hollow Knight'...")
store1.delist_product(g)

print("\n[Active Catalogue After Delist]:")
store1.display()

print("\n[Delisted Archive After Delist]:")
store1.display_delisted()

print("\n" + "="*50 + "\n")

print("--- Relisting Test ---")
print("Relisting 'Hollow Knight'...")
store1.relist_product(g)

print("\n[Active Catalogue After Relist]:")
store1.display()

print("\n[Delisted Archive After Relist]:")
store1.display_delisted()

print("\n" + "="*50 + "\n")

print("--- Type Safety & Exception Handling Test ---")
try:
    # Attempting to add an invalid object type
    store1.add_product("This is just a random string, not a Product instance")
except TypeError as e:
    print(f"Successfully caught expected TypeError: {e}")