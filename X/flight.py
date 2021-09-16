class Flight:

    def __init__(self, capacity,):
        self.capacity = capacity
        self.passengers =[]
        
    def open_seats(self):
        return self.capacity - len(self.passengers)
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

flight=Flight(2)
people=["Harry", "Ron", "Hermione", "Ginny", 'gg']
for person in people:
    if flight.add_passenger(person):
        print("Added {person} to flight.")
    else:
        print("No available seats for {person}.")			

 import os
os.system('pause')

