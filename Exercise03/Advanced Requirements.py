'''Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens?
How can you handle multiple words in Python? 
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?'''

# Get user details
def get_user_details():
    # Input full name; use .split to handle first and last names
    full_name = input("Enter your full name (e.g., Muhammad Abbas): ")
    name_parts = full_name.split(maxsplit=1)  # Split into first and last name
    
    # Assign names, handling cases where only one name is provided
    f_name = name_parts[0]
    l_name = name_parts[1] if len(name_parts) > 1 else "No last name provided"
    
    # Input for hometown
    hometown = input("Enter your hometown: ").strip() 
    
    # Validate age input to ensure it is a number
    while True:
        age = input("Enter your age (must be a number): ").strip()  # .strip() removes any leading or trailing whitespace.
        if age.isdigit():  # Check if input is all digits
            age = int(age)  # Convert to integer
            break  # Break will stop the loop once a valid age is entered
        print("Invalid input! Please enter a valid number for age.")
    
    # Display user information
    print("\nYour Information:")
    print(f"Name: {f_name} {l_name}")
    print(f"Hometown: {hometown}")
    print(f"Age: {age}")

# Call the function to get user data
get_user_details()