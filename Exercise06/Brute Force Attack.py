'''Exercise 6: Brute Force Attack - 30 Marks
Write a program that simulates a password entry system. The correct password is defined as 12345. 
The program should keep asking the user to enter the password until they provide the correct one.

Basic Requirements:
Define the correct password.
Use a while loop to repeatedly ask the user for the password until the correct one is entered.
Output an appropriate message when the correct password is entered.'''

# Define the correct password as a constant
CORRECT_PASSWORD = "12345"

# Start a loop that continues until the correct password is entered
while True:
    # Prompt the user to enter a password
    entered_password = input("Please enter the password: ")
    
    # Check if the entered password matches the correct one
    if entered_password == CORRECT_PASSWORD:
        # If correct, display a success message and exit the loop
        print("Permission to enter granted. Good day!")
        break  # Exit the loop
    else:
        # If incorrect, let the user know and prompt again
        print("Incorrect password. Please try again.")
