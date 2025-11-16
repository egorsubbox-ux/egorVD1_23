import random

from VD_games.engine import run_game


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_gcd_question():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    correct_answer = gcd(a, b)
    question = f"{a} {b}"
    return question, str(correct_answer)


def main():
    run_game(
        'Find the greatest common divisor of given numbers.',
        generate_gcd_question
    )


if __name__ == '__main__':
    main()
