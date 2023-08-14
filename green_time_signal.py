def adjust_green_signal_time(vehicle_count):
    base_green_time = 30  # Base green time in seconds
    vehicle_multiplier = 2  # Green time increases by 2 seconds per vehicle
    
    green_time = base_green_time + (vehicle_count * vehicle_multiplier)
    return green_time

def main():
    try:
        with open("vehicle_count.txt", "r") as file:
            vehicle_count = int(file.read())
            
            if vehicle_count < 0:
                print("Invalid vehicle count in the file. Please ensure the count is a non-negative integer.")
                return
        
        green_time = adjust_green_signal_time(vehicle_count)
        print("Adjusted Green Signal Time:", green_time, "seconds")
    except (ValueError, FileNotFoundError):
        print("Error reading vehicle count from file.")

if __name__ == "__main__":
    main()
