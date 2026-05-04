from classes import *

# Create station
station1 = Station(1, "Main Station", 2)

# Create scooters
scooter1 = Scooter(101, 80, "available", "Station", "standard")
scooter2 = Scooter(102, 90, "available", "Station", "premium")

# Add scooters to station
station1.add_scooter(scooter1)
station1.add_scooter(scooter2)

# Try adding extra scooter (capacity check)
extra_scooter = Scooter(103, 70, "available", "Station")
station1.add_scooter(extra_scooter)

# Create user
user1 = Member(1, "Ali")

# Reserve scooter
reservation = user1.reserve_scooter(scooter1)

# Try renting reserved scooter (should fail)
user1.rent_scooter(scooter1)

# Set scooter back to available manually for testing
scooter1.status = "available"

# Rent scooter
rental = user1.rent_scooter(scooter1)

# End rental with duration
if rental:
    rental.end_rental(duration=2)

# Try renting same scooter again (should work now)
user1.rent_scooter(scooter1)

# Report maintenance
maintenance = MaintenanceRecord(scooter1, "Battery issue")

# Try renting scooter in maintenance (should fail)
user1.rent_scooter(scooter1)