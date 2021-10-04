from random import randrange


RULES = 'What number is missing in the progression?'
SERIES_AMOUNT_BEGIN = 5
SERIES_AMOUNT_LIMIT = 11
DIFFERENCE_BEGIN = 2
DIFFERENCE_LIMIT = 16
FIRST_NUMBER_BEGIN = 2
FIRST_NUMBER_LIMIT = 30


def get_arithmetic_series():
    series_amount = randrange(SERIES_AMOUNT_BEGIN, SERIES_AMOUNT_LIMIT)
    difference = randrange(DIFFERENCE_BEGIN, DIFFERENCE_LIMIT)
    first_number = randrange(FIRST_NUMBER_BEGIN, FIRST_NUMBER_LIMIT)
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
    arithmetic_series = get_arithmetic_series()
    missing_number = randrange(len(arithmetic_series))
    answer = str(arithmetic_series[missing_number])
    arithmetic_series[missing_number] = '..'
    return convert_arithmetic_series_to_string(arithmetic_series), answer
