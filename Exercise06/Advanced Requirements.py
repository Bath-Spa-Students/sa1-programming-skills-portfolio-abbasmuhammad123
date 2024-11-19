'''Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. 
If the maximum number of attempts is reached, inform the user that the authorities have been alerted.'''

# Define the correct password
correct_password = "abbas"

# Set the maximum number of allowed attempts
max_attempts = 5

# Initialize the attempt counter
attempts = 0

# Start a loop that continues until the correct password is entered or the attempts run out
while attempts < max_attempts:
    # Prompt the user to enter the password, simulate a masked input by showing '*' for each character
    user_password = input("Please enter the password: ").strip()#Prompt the user to enter the password and remove any extra spaces before or after the input
    masked_password = '*' * len(user_password)  # hide the entered password

    # Increment the attempt counter
    attempts += 1

    # Check if the entered password matches the correct password
    if user_password == correct_password:
        # If correct, display a success message and exit the loop
        print("Access granted. Welcome User!")
        break
    else:
        # If incorrect, inform the user and show the masked password
        print(f"Incorrect password: {masked_password}")
        
        # Calculate and inform the user of the remaining attempts
        remaining_attempts = max_attempts - attempts
        print(f"You have {remaining_attempts} attempt(s) remaining.")

        # Provide a hint if the user has only one attempt left
        if attempts == max_attempts - 1:
            print("Hint: The password is a name.")

        # If the maximum attempts are reached, lock the user out
        if attempts == max_attempts:
            print("Access denied. You have been locked out.")
            print("Maximum attempts reached. Authorities have been alerted.")
