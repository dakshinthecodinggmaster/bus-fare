class Vehicle:
    def __init__(self, fare):
        self.fare = fare

class Bus(Vehicle):
    def total_fare(self):
        return self.fare + (0.10 * self.fare)