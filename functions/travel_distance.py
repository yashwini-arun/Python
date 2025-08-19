def calculate_distance(speed, time):
    return speed * time

def calculate_time(distance, speed):
    return distance / speed

# Main program
choice = input("Find (D)istance or (T)ime? ").lower()

if choice == "d":
    speed = float(input("Enter speed (km/h): "))
    time = float(input("Enter time (hours): "))
    print("Distance:", calculate_distance(speed, time), "km")
elif choice == "t":
    distance = float(input("Enter distance (km): "))
    speed = float(input("Enter speed (km/h): "))
    print("Time:", calculate_time(distance, speed), "hours")
