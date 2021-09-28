#!/usr/bin/env python
"""Game: Parity check."""
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_COUNT = 1
LIMIT = 21


def question(number):
    return number[0]


def right_answer(number):
    number = number[0]
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer
