import prompt


def welcome():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def run(question, answer, name):
    print('Question: ' + str(question))
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print('Correct!')
        return 1
    else:
        print("'{}' is wrong answer ;(. "
              "Correct answer was '{}'".format(user_answer, answer))
        print("Let's try again, {}!".format(name))
        return 0


def finish(win, name):
    if win == 3:
        print('Congratulations, {}!'.format(name))
