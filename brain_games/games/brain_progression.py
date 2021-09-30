from random import randrange


RULES = 'What number is missing in the progression?'
NUMBER_COUNT = 1
LIMIT = 30
START_NUMBER = 2


def get_question_and_answer(question_array):
    sequence_amount = randrange(5, 11)
    step = randrange(2, 11)
    missing_number = randrange(sequence_amount)
    for i in range(sequence_amount - 1):
        question_array.append(question_array[i] + step)
    question_array[missing_number], answer = (
        '..',
        str(question_array[missing_number]))
    question = ''
    for i in range(len(question_array)):
        if i < len(question_array) - 1:
            question += str(question_array[i]) + ' '
        else:
            question += str(question_array[i])
    return question, answer
