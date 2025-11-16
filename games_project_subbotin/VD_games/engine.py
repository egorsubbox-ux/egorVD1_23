from VD_games.cli import welcome_user


def run_game(game_description, generate_question):
    name = welcome_user()
    print(game_description)
    correct_answers_count = 0
    rounds_to_win = 3
    while correct_answers_count < rounds_to_win:
        question, correct_answer = generate_question()
        print(f'Question: {question}')
        user_answer = input('Your answer: ').strip().lower()
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
