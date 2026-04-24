# Maximum capacity
max_capacity = 5

# Authorized IDs
authorized_ids = ["ID01", "ID02", "ID03"]

# Incoming guests
incoming_guests = ["ID01", "ID05", "ID02", "ID07", "ID03", "ID08", "ID02"]

# Counter for entered guests
count = 0

# Loop through guests
for guest in incoming_guests:
    
    if count == max_capacity:
        print("Capacity Reached. No more entries allowed.")
        break

    if guest in authorized_ids:
        print(f"{guest}: Access Granted")
        count += 1
    else:
        print(f"{guest}: Access Denied")