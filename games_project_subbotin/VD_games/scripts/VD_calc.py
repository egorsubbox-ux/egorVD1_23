import random

from VD_games.engine import run_game


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


def main():
    run_game(
        'What is the result of the expression?',
        generate_expression
    )


if __name__ == '__main__':
    main()
