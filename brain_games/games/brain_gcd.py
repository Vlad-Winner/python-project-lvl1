"""Game GCD."""
from random import randrange


RULES = 'Find the greatest common divisor of given numbers.'


def get_gcd(one, two):
    if one > two:
        one, two = two, one
    while two % one != 0:
        two, one = one, two % one
    divider = one
    return divider


def get_question_and_answer():
    numbers = []
    for i in range(2):
        numbers.append(randrange(1, 50))
    question = str(numbers[0]) + ' ' + str(numbers[1])
    answer = str(get_gcd(numbers[0], numbers[1]))
    return question, answer
