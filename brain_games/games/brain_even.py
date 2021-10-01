"""Game: Parity check."""
from random import randrange


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randrange(1, 21)
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
