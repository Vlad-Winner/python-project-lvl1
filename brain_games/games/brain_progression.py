from random import randrange


RULES = 'What number is missing in the progression?'


def get_arithmetic_series():
    series_amount = randrange(5, 11)
    difference = randrange(2, 16)
    first_number = randrange(2, 30)
    arithmetic_series = [first_number]
    for i in range(series_amount):
        arithmetic_series.append(arithmetic_series[i] + difference)
    return arithmetic_series


def convert_arithmetic_series_to_string(arithmetic_series):
    arithmetic_series_str = ''
    for i in range(len(arithmetic_series)):
        if i < len(arithmetic_series) - 1:
            arithmetic_series_str += str(arithmetic_series[i]) + ' '
        else:
            arithmetic_series_str += str(arithmetic_series[i]) + ' '
    return arithmetic_series_str


def get_question_and_answer():
    question = get_arithmetic_series()
    missing_number = randrange(len(question))
    question[missing_number], answer = (
        '..',
        str(question[missing_number]))
    return convert_arithmetic_series_to_string(question), answer
