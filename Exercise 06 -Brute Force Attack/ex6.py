# Set the correct password
correct_password = "0608"

# Set how many attempts the user has
attempts = 5

# Loop runs while the user still has attempts left
while attempts > 0:

    # Ask the user for the password
    password = input("Enter the password: ")

    # Check if the password is correct
    if password == correct_password:
        print("Access granted.")
        break  # Stop the loop because the user got it right

    else:
        attempts -= 1 # If the password is wrong, remove one attempt

        # If there are attempts left, tell the user
        if attempts > 0:
            print(f"Wrong password. Attempts left: {attempts}")

        # If no attempts remain, alert the user
        else:
            print("Too many failed attempts. Authorities have been alerted.")
