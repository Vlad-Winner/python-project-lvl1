"""Game GCD."""
RULES = 'Find the greatest common divisor of given numbers.'
NUMBER_COUNT = 2
LIMIT = 50


def correct_answer(one, two):
    if one > two:
        one, two = two, one
    divider = one
    while one % divider != 0 or two % divider != 0:
        divider -= 1
    return divider


def main(numbers):
    question = str(numbers[0]) + ' ' + str(numbers[1])
    answer = str(correct_answer(numbers[0], numbers[1]))
    return question, answer
