'''Exercise 3: Biography - 25 Marks
In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

Steps:
Store the information (name, hometown, and age) as key-value pairs in a dictionary.
Print the values on separate lines using a single print() statement.
Use variables with appropriate data types for each piece of information.'''

# Step 1: Define variables for each piece of information
name = "Muhammad Abbas" # String for the name
hometown = "Pakistan"   # String for the hometown
age = 19                 # Integer for the age
father_name = "Ghulam Shabbir"  # String for father name
country_of_residence = "United Arab Emirates" # String for country of residence

# Step 2: Store information in a dictionary with key-value pairs
bio = {
    "Name": name, # Key 'name' with the value of the name variable
    "Hometown": hometown, # Key 'hometown' with the value of the hometown variable
    "Age": age, # Key 'age' with the value of the age variable
    "FatherName": father_name, # Key 'FatherName' with the value of the father_name variable
    "CountryOfResidence": country_of_residence # Key 'CountryOfResidence' with the value of the country_of_residence variable
}

# Step 3: Print each value on separate lines using a single print statement
# Using f-strings to display each value on a new line
print(f"{bio['Name']}\n{bio['Hometown']}\n{bio['Age']}\n{bio['FatherName']}\n{bio['CountryOfResidence']}")
