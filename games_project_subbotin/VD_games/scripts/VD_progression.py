import random

from VD_games.engine import run_game


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression = []
    for i in range(length):
        progression.append(start + i * step)

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))
    return question, str(correct_answer)


def main():
    run_game(
        'What number is missing in the progression?',
        generate_progression
    )


if __name__ == '__main__':
    main()
