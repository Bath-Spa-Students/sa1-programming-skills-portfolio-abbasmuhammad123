'''Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, 
ask the user if the year is a leap year and adjust the number of days accordingly.'''

# Dictionary mapping month numbers (1-12) to days (non-leap year)
days_in_month = {
    1: 31,   # January
    2: 28,   # February
    3: 31,   # March
    4: 30,   # April
    5: 31,   # May
    6: 30,   # June
    7: 31,   # July
    8: 31,   # August
    9: 30,   # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Ask the user for the month number
try:
    month_number = int(input("Enter the month number (1-12): ").strip())

    # Check if the month is valid
    if 1 <= month_number <= 12:
        
        # Check if the selected month is February
        if month_number == 2:
            # Ask if it's a leap year
            is_leap = input("Is it a leap year? (yes/no): ").strip().lower()
            # Adjust days for February in leap year
            days = 29 if is_leap == "yes" else 28
        else:
            # For other months, get days from dictionary
            days = days_in_month[month_number]
        
        print(f"The number of days in month {month_number} is {days}.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")

except ValueError:
    print("Invalid input. Please enter a numeric month number between 1 and 12.")

