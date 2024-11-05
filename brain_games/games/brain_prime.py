from brain_games.game_engine import game_engine, ROUNDS_COUNT
from brain_games.utils import get_random_number


DESC = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 1:
        return False
    for i in range(2, (number // 2) + 1):
        if (number % i) == 0:
            return False
    return True


def generate_rounds():
    i = 0
    data = []
    for i in range(ROUNDS_COUNT):
        i += 1

        question = get_random_number()
        answer = 'yes' if is_prime(question) else 'no'
        data.append((question, answer))
    return data


def main():
    rounds = generate_rounds()
    game_engine(rounds, DESC)
