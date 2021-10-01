import prompt
from random import randrange


ROUND_COUNT = 3


def generate_number(count, limit, start_number):
    numbers = []
    for i in range(count):
        numbers.append(randrange(start_number, limit))
    return numbers


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.RULES)
    win = 0
    for i in range(ROUND_COUNT):
        question, right_answer = game.get_question_and_answer()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
            win += 1
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'".format(user_answer, right_answer))
            print("Let's try again, {}!".format(name))
            break
    if win == ROUND_COUNT:
        print('Congratulations, {}!'.format(name))
