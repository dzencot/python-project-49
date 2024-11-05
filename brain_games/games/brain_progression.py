from brain_games.game_engine import game_engine, ROUNDS_COUNT
from brain_games.utils import get_random_number


DESC = 'What number is missing in the progression?'


def get_progression(start, step, length=10):
    current = start
    progression = []
    while len(progression) < length:
        progression.append(current)
        current += step
    return progression


def generate_rounds():
    i = 0
    data = []
    for i in range(ROUNDS_COUNT):
        i += 1

        start = get_random_number()
        step = get_random_number()
        progression = get_progression(start, step)
        hidden_index = get_random_number(0, len(progression) - 1)
        hidden_number = progression[hidden_index]
        progression[hidden_index] = '..'
        question_data = []
        for item in progression:
            question_data.append(str(item))

        question = ' '.join(question_data)
        answer = str(hidden_number)
        data.append((question, answer))
    return data


def main():
    rounds = generate_rounds()
    game_engine(rounds, DESC)
