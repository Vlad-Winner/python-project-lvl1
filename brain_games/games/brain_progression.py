#!/usr/bin/env python
from random import randrange
from brain_games.scripts import logic


def main():
    name = logic.welcome()
    print('What number is missing in the progression?')
    win = 0
    for i in range(3):
        sequence_amount = randrange(5, 11)
        step = randrange(2, 11)
        missing_number = randrange(sequence_amount)
        start_sequence = randrange(2, 30)
        question_array = [start_sequence]
        for j in range(sequence_amount - 1):
            question_array.append(question_array[j] + step)
        question_array[missing_number], answer = (
            '..',
            str(question_array[missing_number]))
        question = ''
        for k in range(len(question_array)):
            if k < len(question_array) - 1:
                question += str(question_array[k]) + ' '
            else:
                question += str(question_array[k])
        if logic.run(question, answer, name):
            win += 1
        else:
            break
    logic.finish(win, name)


if __name__ == '__main__':
    main()
