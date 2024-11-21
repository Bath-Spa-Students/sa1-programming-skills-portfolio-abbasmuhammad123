'''Loops- Pizza Toppings :
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.'''

# Loop to ask for pizza toppings until the user enters 'quit'
while True:
    topping = input("Enter a pizza topping (or 'quit' to stop): ")

    # Check if the user wants to quit
    if topping.lower() == 'quit':
        print("Stopping pizza topping selection.")
        break

    # Otherwise, print the message
    print(f"Adding {topping} to your pizza!")
