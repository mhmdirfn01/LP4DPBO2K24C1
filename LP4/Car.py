from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, plate_number, brand, year, color, num_seats, num_doors):
        super().__init__(plate_number, brand, year, color)
        self.num_seats = num_seats
        self.num_doors = num_doors

    def display_info(self):
        print("Car Information:")
        print(f"Plate Number: {self.plate_number}")
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Number of Seats: {self.num_seats}")
        print(f"Number of Doors: {self.num_doors}")
