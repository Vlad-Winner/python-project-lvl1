import prompt
from random import randrange


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def generate_number(count, limit):
    numbers = []
    for i in range(count):
        numbers.append(randrange(1, limit))
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
    if win == 3:
        print('Congratulations, {}!'.format(name))


def run(game):
    name = welcome()
    print(game.RULES)
    win = 0
    for i in range(3):
        numbers = generate_number(game.NUMBER_COUNT, game.LIMIT)
        if is_correct(game.question(numbers),
                      game.right_answer(numbers),
                      name):
            win += 1
        else:
            break
    finish(win, name)
