'''Exercise 8: Simple Search - 30 Marks
Write a program that searches for a specific string within a list of strings. The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). 
, and your task is to search for "Sam".'''

# Declare an array of strings with a size of 6 and assign values
names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]  # Array initialized with names

# Ask the user to input the string to search for
search_term = input("Enter the name you want to search for: ")

# Iterate through the array using a for loop
# The loop is explicitly set to run for the length of the array (6 iterations in this case)
for i in range(len(names)):
    # Check if the current name matches the search term
    if names[i] == search_term:
        # Output a success message with the position of the found term
        print(f"'{search_term}' found at index {i} in the array.")
        break  # Exit the loop since the term is found
else:
    # This else block executes if the for loop completes without a break
    print(f"'{search_term}' not found in the array.")
