"""Game calculate."""
from random import choice


RULES = 'What is he result of the expression?'
NUMBER_COUNT = 2
LIMIT = 55


def main(number):
    arguments = ['+', '-', '*']
    argument = choice(arguments)
    if argument == '-':
        question = str(number[0]) + ' - ' + str(number[1])
        answer = str(number[0] - number[1])
    elif argument == '+':
        question = str(number[0]) + ' + ' + str(number[1])
        answer = str(number[0] + number[1])
    elif argument == '*':
        question = str(number[0]) + ' * ' + str(number[1])
        answer = str(number[0] * number[1])
    return question, answer
