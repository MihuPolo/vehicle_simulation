# vehicle.py

class Vehicle:
    def __init__(self, id, password, certificate):
        self.id = id
        self.password = password
        self.certificate = certificate

    def __str__(self):
        return f"Vehicle {self.id}"
