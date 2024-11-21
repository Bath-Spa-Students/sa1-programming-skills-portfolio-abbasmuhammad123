'''Control Structures:
Imagine an alien was just shot down in a game. Create a variable called alien_color and
assign it a value of 'green', 'yellow', or 'red'.'''

# ask the user to input the alien's color
a_color = input("Enter the alien's color (green, yellow, red): ").lower()

# Use an if-else statement to respond based on the alien's color
if a_color == "green":
    print("You just earned 5 points!")
elif a_color == "yellow":
    print("You just earned 10 points!")
elif a_color == "red":
    print("You just earned 15 points!")
else:
    print("Invalid alien color! No points earned.")
