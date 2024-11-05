import prompt


ROUNDS_COUNT = 3


def game_engine(game_rounds, description):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(description)

    for game_round in game_rounds:
        (question, answer) = game_round
        user_answer = prompt.string(f'Question: {question}\n')
        print(f'Your answer: {user_answer}')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(.Correct answer was '{answer}'.")  # noqa: E501
            print("Let's try again, Bill!")
            return
        print('Correct!')

    print(f'Congratulations, {name}!')
