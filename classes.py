# Classes for Scooter Rental System

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Member(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.rentals = []
        self.reservations = []

    def rent_scooter(self, scooter):
        # Prevent renting if scooter not available
        if scooter.status != "available":
            print("Scooter not available")
            return None

        scooter.status = "in use"
        rental = Rental(self, scooter)
        self.rentals.append(rental)
        print(self.name, "rented scooter", scooter.scooter_id)
        return rental

    def reserve_scooter(self, scooter):
        # Prevent reservation conflict
        if scooter.status != "available":
            print("Scooter cannot be reserved")
            return None

        reservation = Reservation(self, scooter)
        self.reservations.append(reservation)
        print(self.name, "reserved scooter", scooter.scooter_id)
        return reservation


class Scooter:
    def __init__(self, scooter_id, battery_level, status, location, scooter_type="standard"):
        self.scooter_id = scooter_id
        self.battery_level = battery_level
        self.status = status
        self.location = location
        self.scooter_type = scooter_type  # type affects cost


class Station:
    def __init__(self, station_id, name, capacity):
        self.station_id = station_id
        self.name = name
        self.capacity = capacity
        self.scooters = []

    def add_scooter(self, scooter):
        # Check station capacity
        if len(self.scooters) >= self.capacity:
            print("Station is full")
            return False

        self.scooters.append(scooter)
        print("Scooter added to station")
        return True


class Rental:
    def __init__(self, user, scooter):
        self.user = user
        self.scooter = scooter
        self.start_time = 0
        self.end_time = None
        self.cost = 0

    def end_rental(self, duration):
        # Calculate cost based on duration and scooter type
        rate = 5

        if self.scooter.scooter_type == "premium":
            rate = 10

        self.cost = duration * rate
        self.end_time = duration

        self.scooter.status = "available"

        print("Rental ended. Cost:", self.cost)


class Reservation:
    def __init__(self, user, scooter):
        self.user = user
        self.scooter = scooter

        scooter.status = "reserved"


class MaintenanceRecord:
    def __init__(self, scooter, issue):
        self.scooter = scooter
        self.issue = issue

        scooter.status = "maintenance"