#!/usr/share/env python3


"""
Arithmetic Quiz - A mini quiz on evaluating arithmetic mathematical expressions written using python.

author: Ashwani Gupta
version: 0.1

"""

import random
import os

# Constants
NUMBER_OF_QUESTIONS = 10
MIN_OPERANDS = 2
MAX_OPERANDS = 10
EASY_RANGE_MIN = 1
EASY_RANGE_MAX = 20
HARD_RANGE_MIN = 20
HARD_RANGE_MAX = 100

def generate_random_integer_in_range(min, max):
    """ (int, int) -> int

    Generate a random integer within range [min, max]
    """

    return random.randint(min, max)


def choose_level():
    """ None -> int

    Ask the user's difficulty level choice. 1 signifies easy level and 2 signifies hard level
    """

    while True:
        print('How difficult do you want the questions to be?')
        print('> Press 1 for EASY or')
        print('> Press 2 for HARD\n')

        choice = int(input('Enter your choice: '))
        print()

        if(choice == 1 or choice == 2):
            return choice
        else:
            print('**Invalid choice. Please try again.')


def ask_question(number_of_operands, level):
    """ (int, int) -> str

    Generate a question based on number of operands and given difficulty level. Return a string representation
    of the question i.e. an arithmetic expression. The operands and operators is chosen randomly.
    """

    # Initialize question
    question = []

    for index in range(2 * number_of_operands - 1):

        # If index is odd, place an operand else place an operator
        if index % 2 != 0:
            operator = generate_random_integer_in_range(0, 3)
            if operator == 0:
                element = '+'
            elif operator == 1:
                element = '-'
            elif operator == 2:
                element = '*'
            elif operator == 3:
                element = '/'
        else:
            if level == 1:
                element = str(generate_random_integer_in_range(EASY_RANGE_MIN, EASY_RANGE_MAX))
            else:
                element = str(generate_random_integer_in_range(HARD_RANGE_MIN, HARD_RANGE_MAX))

        question.append(element)

    # Return a string representation of the arithmetic expression
    return ' '.join(question)


def calculate_answer(question):
    """ str -> int

    Calculate the answer of the arithmetic expression given as the question. Return the result as integer.
    """

    # Replace single slash '/' with double slash '//' for integer division in python 3
    question = question.replace('/', '//')

    # Evaluate the answer
    answer = eval(question)

    return answer


def play_game():
    """ None -> None

    Start the qrithmetic quiz game.
    """

    while True:

        os.system('clear')
        welcome_msg = """Welcome to Arithmetic Quiz.\n\nInstructions:\n=============\n\
    1. Choose a level of difficulty (easy or hard).\n\
    2. Evaluate the given mathematical expression using your mind. You can use pen/pencil/paper.\n\
    3. Enter the answer you got. If it is correct, you will get points. There are total of ten questions. For each correct answer you will get 1 point.\n\
    4. You need to score more than 50% to pass the quiz.
    5. Lastly, please do not use any kind of calculator. You cannot enjoy the quiz if you are cheating.\n\
    6. Let's begin the game. Enjoy :)"""
        print(welcome_msg)
        print()

        # Player chooses difficulty level
        level = choose_level()

        score = 0
        question_count = 1

        while question_count <= NUMBER_OF_QUESTIONS:

            # Print question number
            print('Question no: ' + str(question_count))
            print('----------------')

            # Generate a random arithmetic expression question
            number_of_operands = generate_random_integer_in_range(MIN_OPERANDS, MAX_OPERANDS);
            question = ask_question(number_of_operands, level)
            print('Evaluate this expression: ' + question)

            try:
                given_answer = int(input('Enter your answer: '))
            except ValueError:
                print("Invalid input. Skipping this question :/")
                print('Current score: ' + str(score) + '\n')
                question_count = question_count + 1
                continue

            actual_answer = calculate_answer(question)
            print()

            # Check if user's answer and actual answer match
            if given_answer == actual_answer:
                print('Correct! Nicely done, how do you do it so easily!!')
                score = score + 1
            else:
                print('Oops! That\'s WRONG! :(')
                print('Correct answer is: ' + str(actual_answer))
            print('Current score: ' + str(score) + '\n')

            question_count = question_count + 1

        # Calculate accuracy and grade
        print('GAME OVER!!')
        accuracy = (score / NUMBER_OF_QUESTIONS) * 100
        print('Your accuracy is: ' + str(accuracy) + '%')

        if accuracy >= 80:
            print('Congratulations! You got grade \'AA\'')
        elif accuracy > 50:
            print('Not bad, keep practising. You got grade \'A\'')
        else:
            print('You failed. You got grade \'B\' :(')
        print()

        # Prompt user if he wants to play again
        while True:
            is_playing_again = input('Would you like to play again? (y/n)')
            if is_playing_again == 'y' or is_playing_again == 'n':
                break
            else:
                print('Invalid choice. Please try again')

        if is_playing_again == 'n':
            print('Have a nice day! Good bye :)')
            break


if __name__ == '__main__':
    play_game()
