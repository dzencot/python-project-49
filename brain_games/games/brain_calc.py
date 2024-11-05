from brain_games.game_engine import game_engine, ROUNDS_COUNT
from brain_games.utils import get_random_number


DESC = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def calculate(left_operand, right_operand, operator):
    if operator == '+':
        return left_operand + right_operand
    elif operator == '-':
        return left_operand - right_operand
    elif operator == '*':
        return left_operand * right_operand
    else:
        raise f'Unknown operator {operator}'


def generate_rounds():
    i = 0
    data = []
    for i in range(ROUNDS_COUNT):
        i += 1

        left_operand = get_random_number()
        right_operand = get_random_number()
        index = get_random_number(1, len(OPERATORS) - 1)

        operator = OPERATORS[index]
        question = f'{left_operand} {operator} {right_operand}'
        answer = str(calculate(left_operand, right_operand, operator))
        data.append((question, answer))
    return data


def main():
    rounds = generate_rounds()
    game_engine(rounds, DESC)
