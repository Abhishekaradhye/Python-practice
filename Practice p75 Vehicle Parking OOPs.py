from datetime import datetime

class Vehicle:
    def __init__(self, number, vehicle_type):
        if vehicle_type not in ['car', 'bike', 'truck']:
            raise Exception("Your vehicle is not allowed to enter ! PLease wait outside !!")
        self.number = number
        self.type = vehicle_type
        self.entry_time = datetime.now()

class Parking_lot:
    rates = {'car': 20, 'bike': 10, 'truck': 30}      # These rates are meant to be per hour :)
    def __init__(self):
        self.parked_vehicles = {}
        self.total_earnings = 0

    def park_vehicle(self, number, vehicle_type):
        if number in self.parked_vehicles:
            raise Exception("This mentioned Vehicle is already parked. Please enter valid vehicle details.")
        vehicle = Vehicle(number, vehicle_type)
        self.parked_vehicles[number] = vehicle
        print(f" Vehicle '{number}' ({vehicle_type}) is parked at {vehicle.entry_time.strftime('%H:%M:%S')} on date {vehicle.entry_time.day}.")

    def unpark_vehicle(self, number):
        if number not in self.parked_vehicles:
            raise Exception("The vehicle {number} is not found parked in parking lot.")
        
        vehicle = self.parked_vehicles.pop(number)
        parked_duration = datetime.now() - vehicle.entry_time 
        hours = max(1, parked_duration.total_seconds() // 3600)
        parking_charge = hours * self.rates[vehicle.type]
        self.total_earnings += parking_charge
        print(f"Vehicle {number} ({vehicle.type}) removed after {hours}h. You are to pay parking charges: ₹{parking_charge}.")

    def show_parked_vehicles(self):
        if not self.parked_vehicles:
            raise Exception("NO vehicle currently parked !")
        
        print('Parked Vehicles:')
        for veh in self.parked_vehicles.values():
            print(f"- Vehicle {veh.number} ({veh.type}) parked since {veh.entry_time.day} {veh.entry_time.strftime('%H:%M:%S')}.")

    def get_total_earnings(self):
        print(f"Total earnings from parking business is {self.total_earnings}.")



pl = Parking_lot()

try:
    pl.park_vehicle("MH12AB1234", "car")
    pl.park_vehicle("MH14XY9999", "bike")
    #pl.park_vehicle("MH12AB1234", "truck")  # should raise error: already parked
except Exception as e:
    print(e)

pl.show_parked_vehicles()

try:
    pl.unpark_vehicle("MH14XY9999")
    pl.unpark_vehicle("MH12AB1234")
    # pl.unpark_vehicle("MH12AB1234")  # should raise error: as it is already removed
except Exception as e:
    print(e)

pl.get_total_earnings()
