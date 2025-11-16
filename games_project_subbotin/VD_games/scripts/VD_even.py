import random

from VD_games.engine import run_game


def generate_even_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), correct_answer


def main():
    run_game(
        'Answer "yes" if the number is even, otherwise answer "no".',
        generate_even_question
    )


if __name__ == '__main__':
    main()
