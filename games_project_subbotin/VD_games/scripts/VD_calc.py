#!/usr/bin/env python3
import random
from VD_games.cli import welcome_user


def generate_expression():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = a + b
    elif operation == '-':
        answer = a - b
    else:  # '*'
        answer = a * b
    question = f"{a} {operation} {b}"
    return question, str(answer)


def play_calc_game():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers_count = 0
    rounds_to_win = 3
    while correct_answers_count < rounds_to_win:
        question, correct_answer = generate_expression()
        print(f'Question: {question}')
        user_answer = input('Your answer: ').strip()
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    play_calc_game()


if __name__ == '__main__':
    main()
