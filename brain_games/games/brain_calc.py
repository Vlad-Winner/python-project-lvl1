"""Game calculate."""
from random import choice


RULES = 'What is he result of the expression?'
NUMBER_COUNT = 2
LIMIT = 55
START_NUMBER = 1


def main(number):
    operators = ['+', '-', '*']
    operator = choice(operators)
    question = '{} {} {}'.format(number[0], operator, number[1])
    if operator == '-':
        answer = str(number[0] - number[1])
    elif operator == '+':
        answer = str(number[0] + number[1])
    elif operator == '*':
        answer = str(number[0] * number[1])
    return question, answer
