from bike import Bike
from cyclist import Cyclist

bike1 = Bike('Mountain', 6)
bike2 = Bike('Road', 8)
bike3 = Bike('Hybrid', 7)


cyclist1 = Cyclist(name="Alex", age=28, weight=70.5, proficiency="Intermediate")
cyclist2 = Cyclist(name="Jordan", age=16, weight=55.0, proficiency="Beginner", protective_gear=True)
cyclist3 = Cyclist("Taylor", 22, 68.0, "Advanced", True)

print(bike1)
print(bike2)
print(bike3)
print(cyclist1)
print(cyclist2)
print(cyclist3)

print(repr(bike1))
print(repr(cyclist1))

bike1.change_gear(True)
bike1.change_gear(True)
bike1.change_gear(True)
bike2.change_gear(False)
bike2.change_gear(True)
bike2.change_gear(False)
bike3.change_gear(True)
bike3.change_gear(False)
bike3.change_gear(True)

cyclist2.accelerate()
cyclist1.brake()
cyclist2.turn('left')
cyclist3.turn('right')
cyclist3.toggle_protection()
cyclist1.toggle_protection()

