"""Game: Parity check."""
RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
NUMBER_COUNT = 1
LIMIT = 21
START_NUMBER = 1


def get_question_and_answer(number):
    question = number[0]
    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
