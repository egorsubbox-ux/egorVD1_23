import random

from VD_games.engine import run_game


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_prime_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer


def main():
    run_game(
        'Answer "yes" if given number is prime. Otherwise answer "no".',
        generate_prime_question
    )


if __name__ == '__main__':
    main()
