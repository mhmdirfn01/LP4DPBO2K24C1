class Vehicle:
    def __init__(self, plate_number, brand, year, color):
        self.plate_number = plate_number
        self.brand = brand
        self.year = year
        self.color = color

    def display_info(self):
        pass  # Method ini akan dioverride di kelas turunan
