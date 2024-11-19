'''Exercise 4: Primitive Quiz - 30 Marks
In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

Steps:
Write a program that asks the user "What is the capital of France?" and waits for their response.
If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
If the answer is incorrect, the program should print a message saying the answer is wrong.'''

# Prompt the user with the question about the capital of France
user_answer = input("What is the capital of France? ").strip() # Using .strip() removes any extra whitespace the user may accidentally add.

# Check if the user's answer matches the correct answer (ignoring case sensitivity)
if user_answer.lower() == "paris":
    # If the answer is correct, print a success message
    print("Correct! The capital of France is Paris.")
else:
    # If the answer is incorrect, print a message indicating it is wrong
    print("Wrong answer. The correct answer is Paris.")
