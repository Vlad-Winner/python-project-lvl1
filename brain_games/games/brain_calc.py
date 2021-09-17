#!/usr/bin/env python
"""Game calculate."""
from brain_games.scripts import logic
from random import choice
from random import randrange


def main():
    name = logic.welcome()
    print('What is he result of the expression?')
    win = 0
    for i in range(3):
        number1 = randrange(1, 55)
        number2 = randrange(1, 55)
        arguments = ['+', '-', '*']
        argument = choice(arguments)
        if argument == '-':
            question = str(number1) + ' - ' + str(number2)
            answer = str(number1 - number2)
        elif argument == '+':
            question = str(number1) + ' + ' + str(number2)
            answer = str(number1 + number2)
        elif argument == '*':
            question = str(number1) + ' * ' + str(number2)
            answer = str(number1 * number2)
        if logic.run(question, answer, name):
            win += 1
        else:
            break
    logic.finish(win, name)


if __name__ == '__main__':
    main()
