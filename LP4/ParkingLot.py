class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.vehicles = []

    def park_vehicle(self, vehicle):
        if len(self.vehicles) < self.capacity:
            self.vehicles.append(vehicle)
            print(f"{vehicle.brand} {vehicle.plate_number} has been parked.")
        else:
            print("Penuh bruh gabisa parkir.")

    def display_info(self):
        print(f"Parking Lot Capacity: {self.capacity}")
        print("Vehicles in Parking Lot:")
        for vehicle in self.vehicles:
            print(f"{vehicle.brand} {vehicle.plate_number}")
