"""Game: Parity check."""
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_COUNT = 1
LIMIT = 21
START_NUMBER = 1


def main(number):
    number = number[0]
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer
