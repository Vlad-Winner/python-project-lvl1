import prompt
from random import randrange


ROUND_COUNT = 3


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def generate_number(count, limit, start_number):
    numbers = []
    for i in range(count):
        numbers.append(randrange(start_number, limit))
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
    if win == ROUND_COUNT:
        print('Congratulations, {}!'.format(name))


def run(game):
    name = welcome()
    print(game.RULES)
    win = 0
    for i in range(ROUND_COUNT):
        numbers = generate_number(
            game.NUMBER_COUNT, game.LIMIT, game.START_NUMBER)
        question, right_answer = game.get_question_and_answer(numbers)
        if is_correct(question, right_answer, name):
            win += 1
        else:
            break
    finish(win, name)
