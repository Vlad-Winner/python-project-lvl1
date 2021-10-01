from random import randrange


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def get_question_and_answer():
    question = randrange(2, 300)
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
