from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, plate_number, brand, year, color, type, tank_capacity):
        super().__init__(plate_number, brand, year, color)
        self.type = type
        self.tank_capacity = tank_capacity

    def display_info(self):
        print("Motorcycle Information:")
        print(f"Plate Number: {self.plate_number}")
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Type: {self.type}")
        print(f"Tank Capacity: {self.tank_capacity}")
