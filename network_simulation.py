# network_simulation.py

import random
from database import vehicles, new_vehicles
from vehicle import Vehicle
from controller import CentralHub, connect_to_another_vehicle

def authenticate_vehicle(new_vehicle):
    # Check if the new vehicle's ID matches any vehicle in the vehicles list
    for vehicle in vehicles:
        if vehicle['id'] == new_vehicle['id']:
            # Compare password
            if vehicle['password'] == new_vehicle['password']:
                print(f"[Success] Password for vehicle {new_vehicle['id']} checked successfully.")
            else:
                print(f"[Error] Password for vehicle {new_vehicle['id']} does not match.")
                return False
            
            # Compare certificate
            if vehicle['certificate'] == new_vehicle['certificate']:
                print(f"[Success] Certificate for vehicle {new_vehicle['id']} checked successfully.")
            else:
                print(f"[Error] Certificate for vehicle {new_vehicle['id']} does not match.")
                return False

            return True
    return False


def simulate_connection(new_vehicle, hub):
    # Print the attempt message
    print(f"\nAttempting to connect vehicle {new_vehicle['id']}...")

    # Attempt to authenticate the new vehicle
    if authenticate_vehicle(new_vehicle):
        vehicle_obj = Vehicle(new_vehicle['id'], new_vehicle['password'], new_vehicle['certificate'])

        # Attempt to connect to the central hub
        if hub.connect_vehicle(vehicle_obj):
            print(f"[Success] Vehicle {new_vehicle['id']} connected successfully to the Network.")
            hub.release()  # Release the hub after successful connection
        else:
            # If the hub is busy, connect to another vehicle
            connect_to_another_vehicle(new_vehicle)
    else:
        print(f"[Error] Authentication failed for vehicle {new_vehicle['id']}. Vehicle not connected to the network.")


def run_simulation():
    hub = CentralHub()
    
    # Iterate over all vehicles in the new vehicle list
    for new_vehicle in new_vehicles:
        simulate_connection(new_vehicle, hub)


# Run the simulation
if __name__ == "__main__":
    run_simulation()
