import prompt
from random import randrange


ROUND = 3
START_NUMBER = 1


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def generate_number(count, limit):
    numbers = []
    for i in range(count):
        numbers.append(randrange(START_NUMBER, limit))
    return numbers


def is_correct(question, right_answer, name):
    print('Question: ' + str(question))
    user_answer = prompt.string('Your answer: ')
    if user_answer == right_answer:
        print('Correct!')
        return 1
    else:
        print("'{}' is wrong answer ;(. "
              "Correct answer was '{}'".format(user_answer, right_answer))
        print("Let's try again, {}!".format(name))
        return 0


def finish(win, name):
    if win == ROUND:
        print('Congratulations, {}!'.format(name))


def run(game):
    name = welcome()
    print(game.RULES)
    win = 0
    for i in range(ROUND):
        numbers = generate_number(game.NUMBER_COUNT, game.LIMIT)
        question, right_answer = game.main(numbers)
        if is_correct(question, right_answer, name):
            win += 1
        else:
            break
    finish(win, name)
