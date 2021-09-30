#!/usr/bin/env python
from brain_games import engine
from brain_games.games import brain_even as even


def main():
    engine.run(even)


if __name__ == '__main__':
    main()
