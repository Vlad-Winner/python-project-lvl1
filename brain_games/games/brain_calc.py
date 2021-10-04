"""Game calculate."""
from random import choice
from random import randrange


RULES = 'What is he result of the expression?'
NUMBER_START = 1
NUMBER_LIMIT = 55


def get_question_and_answer():
    operators = ['+', '-', '*']
    operator = choice(operators)
    number_first = randrange(NUMBER_START, NUMBER_LIMIT)
    number_second = randrange(NUMBER_START, NUMBER_LIMIT)
    question = '{} {} {}'.format(number_first, operator, number_second)
    if operator == '-':
        answer = str(number_first - number_second)
    elif operator == '+':
        answer = str(number_first + number_second)
    elif operator == '*':
        answer = str(number_first * number_second)
    return question, answer
