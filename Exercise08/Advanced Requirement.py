'''Optional Requirements:
Allow the user to input the search term instead of using a predefined value.
Implement the search functionality based on user input.'''

# Initialize a predefined list of names
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave", "Abbas"]

# Prompt the user to enter the name they want to search for
search_term = input("Enter the name you want to search for: ").strip()

# Perform the search by checking if the search term exists in the list (case-insensitive)
if search_term.lower() in [name.lower() for name in names]:
    # If found, print a success message
    print(f"{search_term} found in the list!")
else:
    # If not found, print a message indicating this
    print(f"{search_term} not found in the list.")
