# controller.py

import random
from database import vehicles

class CentralHub:
    def __init__(self):
        self.is_busy = False  # Initially, the hub is not busy

    def connect_vehicle(self, vehicle):
        # For vehicle V20, simulate the central hub as always busy
        if vehicle.id == 'V20':
            self.is_busy = True
        else:
            # For all other vehicles, the hub is not busy
            self.is_busy = False
        
        if self.is_busy:
            print(f"[Error] Central Hub is currently busy. Vehicle {vehicle.id} cannot connect.")
            return False
        else:
            print(f"[Central Hub] Vehicle {vehicle.id} attemted to connect to the central hub...")
            return True

    def release(self):
        self.is_busy = False  # Release the hub after the vehicle has connected


def connect_to_another_vehicle(new_vehicle):
    # Select a random connected vehicle from the vehicles list
    connected_vehicles = [v for v in vehicles if v['connected']]
    if connected_vehicles:
        connected_vehicle = random.choice(connected_vehicles)
        print(f"[{new_vehicle['id']}] Attempting to connect to vehicle {connected_vehicle['id']}...")
        
        # Simulate successful connection to the connected vehicle
        print(f"[Success] Password for vehicle {new_vehicle['id']} checked successfully.")
        print(f"[Success] Certificate for vehicle {new_vehicle['id']} checked successfully.")
        print(f"[Success] Vehicle {new_vehicle['id']} connected successfully to vehicle {connected_vehicle['id']}.")
        print(f"Welcome to the network, vehicle {new_vehicle['id']}!")
    else:
        print("[Error] No connected vehicles available to connect to.")
