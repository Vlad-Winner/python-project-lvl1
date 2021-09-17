#!/usr/bin/env python
"""Game: Parity check."""
from random import randrange
import prompt


def main():
    """Start the game."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(3):
        number = randrange(1, 21)
        print('Question: ' + str(number))
        result = prompt.string('Your answer: ')
        if number % 2 == 0:
            even = 'yes'
        else:
            even = 'no'
        if result == even:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(."
                  " Correct answer was '{}'".format(result, even))
            print("Let's try again, {}!".format(name))
            break
    if result == even:
        print('Congratulations, {}!'.format(name))


if __name__ == '__main__':
    main()
