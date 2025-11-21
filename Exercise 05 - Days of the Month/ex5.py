# Dictionary mapping month numbers to days (default February = 28)
months = {
    1: 31,
    2: 28,   # February (changes in leap years)
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

# Ask the user for a month number
month_number = int(input("Enter a month number (1-12): "))

# Check if the month exists
if month_number in months:

    # If February, ask about leap year
    if month_number == 2:
        # Ask the user if it's a leap year
        leap = input("Is it a leap year? (yes/no): ").strip().lower()

        # Adjust February's days if leap year
        if leap == "yes":
            print("Number of days: 29")
        else:
            print("Number of days: 28")

    else:
        # For all other months, just print the days directly
        print(f"Number of days: {months[month_number]}")

else:
    # If the number is not between 1 and 12
    print("Invalid month number.")
