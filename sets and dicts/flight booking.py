
flights = {
    "AI101": {"from": "Delhi", "to": "Mumbai", "seats": set(range(1, 11))},
    "AI202": {"from": "Chennai", "to": "Bangalore", "seats": set(range(1, 6))}
}

print("Available Flights:")
for code, details in flights.items():
    print(code, ":", details)

flight_code = "AI101"
seat_to_book = 5

if seat_to_book in flights[flight_code]["seats"]:
    flights[flight_code]["seats"].remove(seat_to_book)
    print(f"\nSeat {seat_to_book} booked successfully on {flight_code}")
else:
    print("\nSeat not available!")

print("\nUpdated Flight Details:")
for code, details in flights.items():
    print(code, "Seats Left:", details["seats"])
