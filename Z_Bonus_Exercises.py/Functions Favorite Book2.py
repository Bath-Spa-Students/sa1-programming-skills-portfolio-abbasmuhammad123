'''Functions -Favorite Book:
Write a function called favorite_book() that accepts one parameter, title. The function
should print a message, such as One of my'''

# Define the function
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

# Get the book title from the user
user_title = input("Enter your favorite book title: ")

# Call the function with the user input
favorite_book(user_title)
