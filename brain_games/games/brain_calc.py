"""Game calculate."""
from random import choice
from random import randrange


RULES = 'What is he result of the expression?'


def get_question_and_answer():
    operators = ['+', '-', '*']
    operator = choice(operators)
    numbers = []
    for i in range(2):
        numbers.append(randrange(1, 55))
    question = '{} {} {}'.format(numbers[0], operator, numbers[1])
    if operator == '-':
        answer = str(numbers[0] - numbers[1])
    elif operator == '+':
        answer = str(numbers[0] + numbers[1])
    elif operator == '*':
        answer = str(numbers[0] * numbers[1])
    return question, answer
