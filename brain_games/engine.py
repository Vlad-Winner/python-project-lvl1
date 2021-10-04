import prompt


ROUND_COUNT = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(game.RULES)
    for _ in range(ROUND_COUNT):
        question, right_answer = game.get_question_and_answer()
        print('Question: ' + str(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'".format(user_answer, right_answer))
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
