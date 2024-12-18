from transport.vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self, capacity, name):
        super().__init__(capacity, name)
        self.name = name

    def __str__(self):
        return f"Ship(ID: {self.vehicle_id}, Capacity: {self.capacity}, Current Load: {self.current_load}, Name: {self.name})"
