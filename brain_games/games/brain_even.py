from brain_games.game_engine import game_engine
from brain_games.utils import get_random_number


DESC = 'Answer "yes" if the number is even, otherwise answer "no".'
ROUNDS_COUNT = 3


def is_even(number):
    return number % 2 == 0


def generate_rounds():
    i = 0
    data = []
    for i in range(ROUNDS_COUNT):
        i += 1
        question = get_random_number()
        answer = 'yes' if is_even(question) else 'no'
        data.append((question, answer))
    return data


def main():
    rounds = generate_rounds()
    game_engine(rounds, DESC)
