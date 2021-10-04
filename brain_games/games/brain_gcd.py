"""Game GCD."""
from random import randrange


RULES = 'Find the greatest common divisor of given numbers.'
NUMBER_START = 1
NUMBER_LIMIT = 50


def get_gcd(one, two):
    if one > two:
        one, two = two, one
    while two % one != 0:
        two, one = one, two % one
    divider = one
    return divider


def get_question_and_answer():
    number_first = randrange(NUMBER_START, NUMBER_LIMIT)
    number_second = randrange(NUMBER_START, NUMBER_LIMIT)
    question = str(number_first) + ' ' + str(number_second)
    answer = str(get_gcd(number_first, number_second))
    return question, answer
