'''Exercise 10: Is it even? - 35 Marks
Write a program that tests if a value is even or odd. Follow the instructions outlined below:
Instructions:
The program should ask the user for a number from within the main function.
The entered number should be passed to a function that determines if the value is even or odd.
The function should return a message indicating whether the number is even or odd.
The message returned by the function should be printed from within the main function.'''

# Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

# Main function
def main():
    # Ask the user for a number
    user_input = int(input("Enter a number: "))
    
    # Call the function and print the result
    print(check_even_odd(user_input))

# Run the program
if __name__ == "__main__":
    main()

