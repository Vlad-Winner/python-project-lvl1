"""Client action."""
import prompt


def welcome_user():
    """User identification."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
