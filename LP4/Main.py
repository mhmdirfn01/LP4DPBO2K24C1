from Vehicle import Vehicle
from Car import Car
from Motorcycle import Motorcycle
from Garage import Garage
from ParkingLot import ParkingLot

def main():
    # Membuat beberapa kendaraan
    car1 = Car("D01XY", "Supra", 2020, "Merah", 5, 4)
    motorcycle1 = Motorcycle("D456F", "lambo", 2019, "Biru", "Sport", 10)

    # Membuat sebuah garasi
    my_garage = Garage("Garasi Urang", 2)

    # Menambahkan kendaraan ke dalam garasi
    my_garage.add_vehicle(car1)
    my_garage.add_vehicle(motorcycle1)

    # Membuat sebuah tempat parkir
    my_parking_lot = ParkingLot(10)

    # Memarkirkan kendaraan di tempat parkir
    my_parking_lot.park_vehicle(car1)
    my_parking_lot.park_vehicle(motorcycle1)

    # Menampilkan informasi tentang kendaraan, garasi, dan tempat parkir
    print("Informasi tentang Kendaraan:")
    car1.display_info()
    motorcycle1.display_info()

    print("\nInformasi tentang Garasi:")
    my_garage.display_info()
    
    print("\nInformasi tentang Tempat Parkir:")
    my_parking_lot.display_info()
    
    # Menampilkan informasi tentang semua kendaraan di dalam garasi
    print("\nKendaraan di dalam Garasi:")
    my_garage.display_vehicles()
    
    # Menampilkan informasi tentang semua kendaraan yang diparkir di tempat parkir
    print("\nKendaraan di dalam Tempat Parkir:")
    my_parking_lot.display_info()

if __name__ == "__main__":
    main()
