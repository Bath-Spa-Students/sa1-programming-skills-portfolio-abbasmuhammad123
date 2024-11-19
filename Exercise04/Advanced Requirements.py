'''Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct). 
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. 
Provide feedback for each question.'''

# Dictionary to store country-capital pairs for the quiz
# Each key is a country, and each value is its corresponding capital
# A simple quiz program on European capitals

def quiz():
    # List of countries and their capitals
    questions = [
        {"country": "France", "capital": "Paris"},
        {"country": "Germany", "capital": "Berlin"},
        {"country": "Italy", "capital": "Rome"},
        {"country": "Spain", "capital": "Madrid"},
        {"country": "Portugal", "capital": "Lisbon"},
        {"country": "Netherlands", "capital": "Amsterdam"},
        {"country": "Belgium", "capital": "Brussels"},
        {"country": "Sweden", "capital": "Stockholm"},
        {"country": "Austria", "capital": "Vienna"},
        {"country": "Poland", "capital": "Warsaw"}
    ]
    
    # Counter for correct answers
    correct_answers = 0
    
    # Iterate over the questions
    for index, question in enumerate(questions):
        print(f"Question {index + 1}: What is the capital of {question['country']}?")
        
        # Get user input and ignore case
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = question["capital"].lower()
        
        # Check the answer and provide feedback
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer is {question['capital']}.")
        print("-" * 50)  # Separator for readability
    
    # Final score display
    print(f"You answered {correct_answers} out of {len(questions)} questions correctly!")
    print("Thank you for playing!")

# Main program
if __name__ == "__main__":
    print("Welcome to the European Capitals Quiz!")
    
    # Ask User for personal details
    name = input("What's your name? ").strip().capitalize()
    age = input("How old are you? ").strip()
    country = input("Which country are you living in? ").strip().capitalize()
    father_name = input("What is your father's name? ").strip().capitalize()  #Cleans input by removing extra spaces and formats it with the first letter capitalized.
    university = input("What is the name of your university? ").strip().capitalize()
    
    # Personalized introduction
    print("\nThank you for providing your details! Here's what we have:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Country of Residence: {country}")
    print(f"Father's Name: {father_name}")
    print(f"University: {university}")
    print("\nLet's get started with the quiz!")
    print("-" * 50)
    
    # Start the quiz
    quiz()
