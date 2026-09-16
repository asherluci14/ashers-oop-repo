from summoning_ritual import SummoningRitual
from necromancer import Necromancer

from undead import Undead

# 1. Undead Skeleton Warrior (Low-cost physical unit)
skeleton_warrior = SummoningRitual(
    name="Skeleton Warrior",
    undead_name="Skeleton Warrior",
    starting_health=100,
    starting_power=15,
    necrotic_cost=10,
    spirit_cost=0,
    bone_cost=50,
    flesh_cost=0,
    ectoplasm_cost=10
)

# 2. Vengeful Ghost (High-spirit/ectoplasm magic unit)
vengeful_ghost = SummoningRitual(
    name="Vengeful Ghost",
    undead_name="Vengeful Ghost",
    starting_health=60,
    starting_power=30,
    necrotic_cost=15,
    spirit_cost=40,
    bone_cost=0,
    flesh_cost=0,
    ectoplasm_cost=40
)

# 3. Putrid Zombie (High-health tank unit)
putrid_zombie = SummoningRitual(
    name="Putrid Zombie",
    undead_name="Putrid Zombie",
    starting_health=60,
    starting_power=10,
    necrotic_cost=20,
    spirit_cost=0,
    bone_cost=10,
    flesh_cost=60,
    ectoplasm_cost=30
)

# 4. Phantom Guardian (Elite hybrid unit)
phantom_guardian = SummoningRitual(
    name="Phantom Guardian",
    undead_name="Phantom Guardian",
    starting_health=100,
    starting_power=60,
    necrotic_cost=30,
    spirit_cost=30,
    bone_cost=25,
    flesh_cost=0,
    ectoplasm_cost=100
)

# 4. Death Knight (Overpowered boss unit)
death_knight = SummoningRitual(
    name="Death Knight",
    undead_name="Death Knight",
    starting_health=200,
    starting_power=200,
    necrotic_cost=80,
    spirit_cost=80,
    bone_cost=80,
    flesh_cost=80,
    ectoplasm_cost=200
)


necro = Necromancer("Asher")
necro.resources.collect(10000,10000,10000,10000,10000)

necro.summon(phantom_guardian)
necro.summon(vengeful_ghost)
necro.summon(phantom_guardian)
necro.summon(putrid_zombie)
necro.summon(vengeful_ghost)

print(necro.undead)

print(necro.find_undead(4).MAX_HEALTH)  # Should return 80 if inheritance and overriding was successful

necro.find_undead(5).level_up(9, 40, 20)
print(necro.find_undead(5))

necro.find_undead(3).command()
necro.find_undead(4).command()

print("\n\n\n\n\nTESTING SEPARATOR\n\n\n\n")

necro.summon(death_knight)
print(necro.find_undead(6))
necro.find_undead(6).level_up(10, 100, 50)
print(necro.find_undead(6))