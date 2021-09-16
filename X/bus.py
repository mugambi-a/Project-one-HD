class Vehicle:
    def __init__(self, name,speed, mileage):
        self.name = name
        self.speed = speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("Volvo", 200, 15)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.speed, "Mileage:", School_bus.mileage)
print(School_bus.seating_capacity())
