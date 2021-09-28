RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
NUMBER_COUNT = 1
LIMIT = 300
START_NUMBER = 2


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def main(number):
    question = number[0]
    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
