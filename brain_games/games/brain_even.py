#!/usr/bin/env python
"""Game: Parity check."""
from brain_games.scripts import logic
from random import randrange


def main():
    """Start the game."""
    name = logic.welcome()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win = 0
    for i in range(3):
        number = randrange(1, 21)
        if number % 2 == 0:
            answer = 'yes'
        else:
            answer = 'no'
        if logic.run(number, answer, name):
            win += 1
        else:
            break
    logic.finish(win, name)


if __name__ == '__main__':
    main()
