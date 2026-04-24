# Store the correct password
correct_password = "admin123"

# Track number of attempts
attempts = 0

# Allow up to 3 attempts
while attempts < 3:
    user_input = input("Enter password: ")
    
    if user_input == correct_password:
        print("Access Granted")
        break
    else:
        attempts += 1
        remaining = 3 - attempts
        if remaining > 0:
            print(f"Incorrect password. {remaining} attempts remaining.")
        else:
            print("No attempts left.")

# After loop check
if attempts == 3:
    print("System Locked")