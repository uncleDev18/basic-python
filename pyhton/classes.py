class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Brian", "Maureen", "Ivan", "Krystal", "Remar"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfuly.")
    else:
        print(f"No available seats for {person}")