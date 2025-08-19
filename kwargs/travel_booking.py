def travel_booking(**kwargs):
    print("=== Travel Booking ===")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    print("=" * 25)

# Main Program
travel_booking(name="Anjali", destination="Goa", tickets=2, hotel="Taj")
travel_booking(name="Ravi", destination="Manali", tickets=4, car_rental="SUV")
travel_booking(name="Divya", destination="Paris", tickets=1, visa_status="Approved")
