"""Game: Parity check."""
from random import randrange


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_START = 1
NUMBER_LIMIT = 21


def get_question_and_answer():
    question = randrange(NUMBER_START, NUMBER_LIMIT)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
