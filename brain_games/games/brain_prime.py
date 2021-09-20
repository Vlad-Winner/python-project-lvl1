#!/usr/bin/env python
from brain_games.scripts import logic
from random import randrange


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def main():
    name = logic.welcome()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    win = 0
    for i in range(3):
        question = randrange(2, 300)
        if is_prime(question):
            answer = 'yes'
        else:
            answer = 'no'
        if logic.run(question, answer, name):
            win += 1
        else:
            break
    logic.finish(win, name)


if __name__ == '__main__':
    main()
