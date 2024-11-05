from brain_games.game_engine import game_engine, ROUNDS_COUNT
from brain_games.utils import get_random_number


DESC = 'Find the greatest common divisor of given numbers.'


def get_gcd(a, b):
    if (b == 0):
        return abs(a)
    else:
        return get_gcd(b, a % b)


def generate_rounds():
    i = 0
    data = []
    for i in range(ROUNDS_COUNT):
        i += 1

        first_number = get_random_number()
        second_number = get_random_number()

        question = f'{first_number} {second_number}'
        answer = str(get_gcd(first_number, second_number))
        data.append((question, answer))
    return data


def main():
    rounds = generate_rounds()
    game_engine(rounds, DESC)
