"""Game: Parity check."""
from random import randrange


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_START = 1
NUMBER_LIMIT = 21


def is_even(number):
    if number % 2 == 0:
        return 'yes'
    else:
        return 'no'


def get_question_and_answer():
    question = randrange(NUMBER_START, NUMBER_LIMIT)
    return question, is_even(question)
