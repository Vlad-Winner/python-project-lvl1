#!/usr/bin/env python
"""Game GCD."""
from random import randrange
from brain_games.scripts import logic


def correct_answer(one, two):
    if one > two:
        one, two = two, one
    divider = one
    while one % divider != 0 or two % divider != 0:
        divider -= 1
    return divider


def main():
    name = logic.welcome()
    print('Find the greatest common divisor of given numbers.')
    win = 0
    for i in range(3):
        numbers = []
        for i in range(2):
            numbers.append(randrange(1, 50))
        question = str(numbers[0]) + ' ' + str(numbers[1])
        answer = str(correct_answer(numbers[0], numbers[1]))
        if logic.run(question, answer, name):
            win += 1
        else:
            break
    logic.finish(win, name)


if __name__ == '__main__':
    main()
