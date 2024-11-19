'''Exercise 5: Days of the Month - 30 Marks
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

Instructions:
Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
Input Handling: Ask the user to input the month number.
Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.'''

# Define a dictionary where keys are month numbers and values are the number of days in each month
month_days = {
    1: 31,  # January
    2: 28,  # February (not considering leap years for simplicity)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

# Prompt the user to enter a month number (1 to 12)
try:
    month_number = int(input("Enter the month number (1-12): "))
    
    # Check if the entered month number is valid (within the range 1-12)
    if month_number in month_days:
        # Retrieve the number of days for the input month and display it
        print(f"The number of days in month {month_number} is {month_days[month_number]}.")
    else:
        # Handle cases where the input is outside the valid range
        print("Invalid month number! Please enter a number between 1 and 12.")
except ValueError:
    # Handle cases where the input is not a valid integer
    print("Invalid input! Please enter a numeric value.")
