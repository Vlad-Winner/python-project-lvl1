"""Game calculate."""
from random import choice


RULES = 'What is he result of the expression?'
NUMBER_COUNT = 2
LIMIT = 55
START_NUMBER = 1


def main(number):
    arguments = ['+', '-', '*']
    argument = choice(arguments)
    question = '{} {} {}'.format(number[0], argument, number[1])
    if argument == '-':
        answer = str(number[0] - number[1])
    elif argument == '+':
        answer = str(number[0] + number[1])
    elif argument == '*':
        answer = str(number[0] * number[1])
    return question, answer
