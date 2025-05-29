"""
City Transport Pass System

You are building a City Transport Pass System to promote public transport (Bus and Metro)
over private options like Rickshaws.

Each passenger is issued a travel pass that they must use for every ride.

System features:
- Tracks passengers' travel history by transport type and date.
- Applies 30% discount for Bus and 25% discount for Metro if used more than 15 days in a month.
- Allows only 2 discounted rides per day; the third ride and onward will be charged full fare.
- Maintains total fare collected and total revenue earned.
- Designed using object-oriented programming.
"""

from datetime import datetime, timedelta
from collections import defaultdict

class Passenger:
    def __init__(self, name):
        self.name = name
        self.pass_issue_date = datetime.now()
        self.travel_days = set()
        self.daily_travel_count = defaultdict(int)
        self.total_paid = 0
        self.total_discount = 0

    def get_discounted_fare(self, mode, fare):
        today = datetime.today().date()
        self.travel_days.add(today)
        self.daily_travel_count[today] += 1

        if len(self.travel_days) > 15 and self.daily_travel_count[today] < 3:
            if mode.lower() == 'bus':
                discount = 0.3 * fare
                return fare - discount, discount
            elif mode.lower() == 'metro':
                discount = 0.25 * fare
                return fare - discount, discount

        return fare, 0


class TransportSystem:
    def __init__(self):
        self.passengers = {}
        self.total_revenue = 0
        self.total_discount_given = 0
        self.fares = {'bus': 30, 'metro': 50, 'rikshaw': 80}

    def register_passenger(self, name):
        if name in self.passengers:
            print(f"Passenger {name} already has a pass.")
        else:
            self.passengers[name] = Passenger(name)

    def travel(self, name, mode):
        if name not in self.passengers:
            print("Passenger not found. Please register first.")
            return

        if mode.lower() not in self.fares:
            print("Invalid mode of transport.")
            return

        passenger = self.passengers[name]
        fare = self.fares[mode]
        final_fare, discount = passenger.get_discounted_fare(mode, fare)

        passenger.total_paid += final_fare
        passenger.total_discount += discount
        self.total_revenue += final_fare
        self.total_discount_given += discount

        print(f"{name} travelled by {mode}. Fare: Rs.{fare}, "
              f"Discount: Rs.{discount}, Paid: Rs.{final_fare}")

    def get_summary(self):
        print("\nTransport System Summary:")
        print(f"Total Revenue Collected: Rs.{self.total_revenue}")
        print(f"Total Discount Given: Rs.{self.total_discount_given}")

        for name, p in self.passengers.items():
            print(f"\nPassenger: {name}")
            print(f"- Days Traveled: {len(p.travel_days)}")
            print(f"- Total Paid: Rs.{p.total_paid}")
            print(f"- Total Discount Received: Rs.{p.total_discount}")

# Demo 

system = TransportSystem()
system.register_passenger("Amit")
system.register_passenger("Priya")
system.register_passenger("Mr.Perfect")

amit = system.passengers["Amit"]
for i in range(16):
    fake_date = datetime.today().date() - timedelta(days=30 - i)
    amit.travel_days.add(fake_date)
print("(Let's assume Amit travelled for 15 days already for our assumption)")
print("\nAmit's 3 rides today (should get discount only twice):")
for i in range(3):
    system.travel("Amit", "bus")

system.travel("Priya", "rikshaw")
system.travel("Mr.Perfect","metro")

system.get_summary()


# Output :>

(Let's assume Amit travelled for 15 days already for our assumption)

# Amit's 3 rides today (should get discount only twice):
# Amit travelled by bus. Fare: Rs.30, Discount: Rs.9.0, Paid: Rs.21.0
# Amit travelled by bus. Fare: Rs.30, Discount: Rs.9.0, Paid: Rs.21.0
# Amit travelled by bus. Fare: Rs.30, Discount: Rs.0, Paid: Rs.30
# Priya travelled by rikshaw. Fare: Rs.80, Discount: Rs.0, Paid: Rs.80
# Mr.Perfect travelled by metro. Fare: Rs.50, Discount: Rs.0, Paid: Rs.50

# Transport System Summary:
# Total Revenue Collected: Rs.202.0
# Total Discount Given: Rs.18.0

# Passenger: Amit
# - Days Traveled: 17
# - Total Paid: Rs.72.0
# - Total Discount Received: Rs.18.0

# Passenger: Priya
# - Days Traveled: 1
# - Total Paid: Rs.80
# - Total Discount Received: Rs.0

# Passenger: Mr.Perfect
# - Days Traveled: 1
# - Total Paid: Rs.50
# - Total Discount Received: Rs.0

