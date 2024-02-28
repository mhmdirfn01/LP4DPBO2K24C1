class Garage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.vehicles = []

    def add_vehicle(self, vehicle):
        if len(self.vehicles) < self.capacity:
            self.vehicles.append(vehicle)
            print(f"{vehicle.brand} {vehicle.plate_number} has been added to the garage.")
        else:
            print("Penuh bruh gabisa parkir.")

    def display_info(self):
        print(f"Garage Name: {self.name}, Capacity: {self.capacity}")
        print("Vehicles in Garage:")
        for vehicle in self.vehicles:
            print(f"{vehicle.brand} {vehicle.plate_number}")

    def display_vehicles(self):
        print("Vehicles in Garage:")
        for vehicle in self.vehicles:
            print(f"{vehicle.brand} {vehicle.plate_number}")
